# Test results with Maven and JUnit 5

docspine reads the JUnit XML reports that Maven Surefire writes. Two things are needed:
the requirement ID in the test's display name, and Surefire writing display names into
the report. Tested with Maven 3.8, Surefire 3.5.4 and JUnit 5.11 / 5.13.

## 1. The requirement ID in the display name

```java
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class HelloWorldTest {

    @Test
    @DisplayName("REQ-0001: prints \"Hello World!\" followed by a line break to standard output")
    void printsGreeting() {
        // …
    }
}
```

A display name on the class applies to every test in it:
`@DisplayName("REQ-0001 Greeting")` on the class. A test may name several requirements:
`@DisplayName("REQ-0001 REQ-0002 …")`.

`@Tag("REQ-0001")` does not work: Surefire does not write tags into the report.

## 2. Surefire writes display names into the report

In `pom.xml`, under `<build>` → `<plugins>`:

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>3.5.4</version>
  <configuration>
    <statelessTestsetReporter implementation="org.apache.maven.plugin.surefire.extensions.junit5.JUnit5Xml30StatelessReporter">
      <usePhrasedTestCaseMethodName>true</usePhrasedTestCaseMethodName>
    </statelessTestsetReporter>
  </configuration>
</plugin>
```

Without this setting, the report contains the method name (`printsGreeting`) instead of
the display name. The display name of the class is written either way.

Optional, for the console: the line "Running …" shows the class's display name with

```xml
<statelessTestsetInfoReporter implementation="org.apache.maven.plugin.surefire.extensions.junit5.JUnit5StatelessTestsetInfoReporter">
  <usePhrasedClassNameInRunning>true</usePhrasedClassNameInRunning>
</statelessTestsetInfoReporter>
```

## 3. The profile names the reports

In `.docspine/PROFILE.md`:

```yaml
test_reports: [target/surefire-reports]
```

## Workflow

```
mvn test
python3 .docspine/docspine.pyz render
python3 .docspine/docspine.pyz check
```

The report after `mvn test` looks like this:

```xml
<testcase name="REQ-0001: prints &quot;Hello World!&quot; followed by a line break to standard output"
          classname="hello.HelloWorldTest" time="0.007"/>
```
