---
name: maven-junit5
title: Maven with JUnit 5
detect: pom.xml
test_command: mvn verify
test_reports: [target/surefire-reports]
requires: [JDK, Maven 3.8 or later, Python 3.9 or later]
tested_with: [Maven 3.8.7, Surefire 3.5.4, exec-maven-plugin 3.5.0, JUnit 5.11 and 5.13]
---

# Integration: Maven with JUnit 5

Fulfils the integration contract in `.docspine/STANDARD.md` section 11: test results as
JUnit XML reports with the requirement ID in the test name, and `check` in the build
after the tests. `render` stays outside the build.

## Test results

**The requirement ID in the display name:**

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

A display name on the class applies to every test in it. A test may name several
requirements: `@DisplayName("REQ-0001 REQ-0002 …")`. `@Tag("REQ-0001")` does not work:
Surefire does not write tags into the report.

**Surefire writes display names into the report.** In `pom.xml`, under `<build>` →
`<plugins>`:

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

Without this setting, the report contains the method name instead of the display name.
The display name of the class is written either way.

**The profile names the reports.** In `.docspine/PROFILE.md`:

```yaml
test_reports: [target/surefire-reports]
```

## Check in the build

`check` runs in the phase `verify`, after the tests. An error fails the build.

```xml
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>exec-maven-plugin</artifactId>
  <version>3.5.0</version>
  <executions>
    <execution>
      <id>docspine-check</id>
      <phase>verify</phase>
      <goals><goal>exec</goal></goals>
      <configuration>
        <executable>python3</executable>
        <workingDirectory>${project.basedir}</workingDirectory>
        <arguments>
          <argument>.docspine/docspine.pyz</argument>
          <argument>check</argument>
        </arguments>
      </configuration>
    </execution>
  </executions>
</plugin>
```

Workflow:

```
python3 .docspine/docspine.pyz render
mvn verify
```

Verified: with correct documentation the build succeeds and `check` reports `OK`; an
unknown epic (error 3) and a hand-edited generated region (error 11) each fail the build.

Optional, for the console: the line "Running …" shows the class's display name with

```xml
<statelessTestsetInfoReporter implementation="org.apache.maven.plugin.surefire.extensions.junit5.JUnit5StatelessTestsetInfoReporter">
  <usePhrasedClassNameInRunning>true</usePhrasedClassNameInRunning>
</statelessTestsetInfoReporter>
```

## Prerequisites

- JDK and Maven 3.8 or later
- Python 3.9 or later for the checker; the build calls `python3`
