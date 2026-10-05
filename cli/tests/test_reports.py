from __future__ import annotations

from support import PROFILE, REQUIREMENT, ProjectTest, replace, req

from docspine import project

REQ_PATH = "docs/01-goals/requirements/REQ-0001.md"
WITH_REPORTS = PROFILE.replace("language: en\n", "language: en\ntest_reports: [target/surefire-reports]\n")
IMPLEMENTED = replace(REQUIREMENT, "status: planned", "status: implemented")


def report(*cases: str, root: str = "testsuite") -> str:
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<{root} name="hello.HelloWorldTest" tests="{len(cases)}">\n'
            + "\n".join(cases) + f"\n</{root}>\n")


def case(name: str, classname: str = "hello.HelloWorldTest", inner: str = "") -> str:
    return f'  <testcase name="{name}" classname="{classname}" time="0.007">{inner}</testcase>'


class ReportTest(ProjectTest):
    def results(self, files):
        self.write(files)
        proj = project.load(self.root)
        return [(r.req, r.result) for r in proj.results], proj

    def with_report(self, xml: str, **extra):
        files = {".docspine/PROFILE.md": WITH_REPORTS,
                 "target/surefire-reports/TEST-hello.HelloWorldTest.xml": xml}
        files.update(extra)
        return files


@req("REQ-0029")
class ReadReports(ReportTest):
    def test_id_in_test_name_counts(self):
        xml = report(case('REQ-0001: prints &quot;Hello World!&quot; followed by a line break'))
        results, _ = self.results(self.with_report(xml))
        self.assertEqual(results, [("REQ-0001", "passed")])

    def test_id_in_class_name_counts_for_every_case(self):
        xml = report(case("printsGreeting", "REQ-0001 Begrüßung"), case("printsTwice", "REQ-0001 Begrüßung"))
        results, _ = self.results(self.with_report(xml))
        self.assertEqual(results, [("REQ-0001", "passed"), ("REQ-0001", "passed")])

    def test_several_ids_in_one_name(self):
        xml = report(case("REQ-0001 REQ-0002 greeting and exit code"))
        results, _ = self.results(self.with_report(xml))
        self.assertEqual(results, [("REQ-0001", "passed"), ("REQ-0002", "passed")])

    def test_cases_without_id_are_ignored(self):
        results, _ = self.results(self.with_report(report(case("helperWorks"))))
        self.assertEqual(results, [])

    def test_passing_report_proves_implemented_requirement(self):
        xml = report(case("REQ-0001: prints the greeting"))
        self.assertEqual(self.codes(self.with_report(xml, **{REQ_PATH: IMPLEMENTED})), [])

    def test_testsuites_root_and_other_xml_files(self):
        xml = report(case("REQ-0001 ok"), root="testsuites")
        other = {"target/surefire-reports/other.xml": "<coverage/>"}
        results, _ = self.results(self.with_report(xml, **other))
        self.assertEqual(results, [("REQ-0001", "passed")])


@req("REQ-0030")
class Outcomes(ReportTest):
    def test_failure_error_and_skipped(self):
        xml = report(case("REQ-0001 a", inner="<failure message='x'/>"),
                     case("REQ-0002 b", inner="<error message='y'/>"),
                     case("REQ-0003 c", inner="<skipped/>"))
        results, _ = self.results(self.with_report(xml))
        self.assertEqual(results, [("REQ-0001", "failed"), ("REQ-0002", "failed"), ("REQ-0003", "skipped")])

    def test_failed_report_does_not_prove_implemented_requirement(self):
        xml = report(case("REQ-0001 ok"), case("REQ-0001 broken", inner="<failure/>"))
        self.assertEqual(self.codes(self.with_report(xml, **{REQ_PATH: IMPLEMENTED})), [8])


@req("REQ-0031")
class UnreadableReports(ReportTest):
    def test_missing_location(self):
        findings = self.findings({".docspine/PROFILE.md": WITH_REPORTS})
        self.assertEqual([(f.code, f.path) for f in findings], [(10, ".docspine/PROFILE.md")])
        self.assertIn("target/surefire-reports", findings[0].message)

    def test_broken_xml(self):
        findings = self.findings(self.with_report("<testsuite><testcase"))
        self.assertEqual([f.code for f in findings], [10])

    def test_test_reports_must_be_a_list(self):
        profile = PROFILE.replace("language: en\n", "language: en\ntest_reports: target\n")
        self.assertEqual(self.codes({".docspine/PROFILE.md": profile}), [1])


@req("REQ-0038")
class DiscoverReports(ReportTest):
    def test_reports_are_found_without_configuration(self):
        xml = report(case("REQ-0001: prints the greeting"))
        results, _ = self.results({"module-a/target/surefire-reports/TEST-a.xml": xml,
                                   "module-b/build/test-results/test/TEST-b.xml": report(case("REQ-0002 b"))})
        self.assertEqual(sorted(results), [("REQ-0001", "passed"), ("REQ-0002", "passed")])

    def test_other_xml_files_are_ignored(self):
        results, proj = self.results({"pom.xml": "<project><modelVersion>4.0.0</modelVersion></project>",
                                      "docs/x.xml": report(case("REQ-0003 in docs"))})
        self.assertEqual(results, [])
        self.assertEqual(proj.findings, [])

    def test_configured_locations_limit_the_search(self):
        files = self.with_report(report(case("REQ-0001 configured")))
        files["other/target/surefire-reports/TEST-x.xml"] = report(case("REQ-0002 elsewhere"))
        results, _ = self.results(files)
        self.assertEqual(results, [("REQ-0001", "passed")])

    def test_discovered_report_proves_implemented_requirement(self):
        xml = report(case("REQ-0001: prints the greeting"))
        self.assertEqual(self.codes({"app/target/surefire-reports/TEST-a.xml": xml, REQ_PATH: IMPLEMENTED}), [])
