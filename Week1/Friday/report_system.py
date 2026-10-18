"""Test-report system: TestResult, Suite, Reporter (+ subclasses).

Fill in every TODO. Run `python3 check_exercise.py N` after each part.
Until a method is finished it raises NotImplementedError; that is normal.
"""


class TestResult:
    """One test outcome. Validated, with two alternative constructors."""

    # Class variables (shared by every TestResult). Given to you.
    VALID_STATUSES = ("PASS", "FAIL", "SKIPPED", "ERROR")
    total_created = 0

    def __init__(self, test_id, status, duration=0.0, message=""):
        if not TestResult.is_valid_id(test_id):
            raise ValueError("Invalid test ID")
        self._test_id = test_id
        
        self.status = status
        self.duration = duration 
        self.message = message
        
        TestResult.total_created += 1
        
        #  1.1: validate test_id with TestResult.is_valid_id (ValueError if bad)
        #           and store it in self._test_id
        #  1.2: set self.status and self.duration THROUGH the properties below,
        #           so validation runs. Store message as a plain attribute.
        #  1.3: increase TestResult.total_created ONLY after everything above
        #           succeeded (an object that fails validation must not be counted)
        #raise NotImplementedError("TODO 1.1-1.3: write __init__")

    # ---- static helper ----------------------------------------------------
    @staticmethod
    def is_valid_id(test_id):
        """True for text like 'TC-001': 'TC-' followed by one or more digits."""
        return (isinstance(test_id,str) and test_id.startswith("TC-") and len(test_id)>3 and test_id[3:].isdigit())
        # TODO 1.4: return True/False. Never raise, even for None or numbers.
        #raise NotImplementedError("TODO 1.4: write is_valid_id")

    # ---- encapsulated attributes -------------------------------------------
    @property
    def test_id(self):
        # TODO 1.5: return the stored id. Read-only: do NOT write a setter.
        return self._test_id
        #raise NotImplementedError("TODO 1.5: test_id getter")

    @property
    def status(self):
        # TODO 1.6: return the stored status
        return self._status
        #raise NotImplementedError("TODO 1.6: status getter")

    @status.setter
    def status(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid status: ", value)
        value = value.strip().upper()
        
        if value not in TestResult.VALID_STATUSES:
            raise ValueError("Invalid status: ", value)
        
        self._status = value
        # TODO 1.6: must be text; strip and upper-case it; it must be in
        #           VALID_STATUSES, otherwise raise ValueError (include the bad
        #           value in the message). Only then store it in self._status.
        #raise NotImplementedError("TODO 1.6: status setter")

    @property
    def duration(self):
        # TODO 1.7: return the stored duration
        return self._duration
        #raise NotImplementedError("TODO 1.7: duration getter")

    @duration.setter
    def duration(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Duration must be a number")
        
        if value < 0:
            raise ValueError("Duration cannot be negative")
        
        self._duration = float(value)
        # TODO 1.7: not int/float (or a bool) -> TypeError; negative -> ValueError;
        #           otherwise store float(value) in self._duration
        #raise NotImplementedError("TODO 1.7: duration setter")

    @property
    def is_passed(self):
        return self.status == "PASS"
        # TODO 1.8: True only when the status is "PASS". Read-only.
        #raise NotImplementedError("TODO 1.8: is_passed")

    # ---- class methods ------------------------------------------------------
    @classmethod
    def how_many(cls):
        return cls.total_created
        # TODO 1.9: return the class-level counter
       # raise NotImplementedError("TODO 1.9: how_many")

    @classmethod
    def from_dict(cls, data):
        for key in ("test_id", "status"):
            if key not in data:
                raise ValueError("Missing required key: ", key)
            
            return cls(data["test_id"], data["status"], data.get("duration", 0.0), data.get("message", ""))
        
        # TODO 1.10: keys "test_id" and "status" are required (ValueError naming the
        #            missing key); "duration" (default 0.0) and "message"
        #            (default "") are optional. Build the object with cls(...),
        #            NOT TestResult(...).
       # raise NotImplementedError("TODO 1.10: from_dict")

    @classmethod
    def from_csv_line(cls, line):
        parts = [part.strip() for part in line.split(",",3)]
        if len(parts)<2:
            raise ValueError("At least test_id and status are required")
        
        test_id = parts[0]
        status = parts[1]
        duration = float(parts[2]) if len(parts) > 2 and parts[2] else 0.0
        message = parts[3] if len(parts) > 3 else ""
        return cls(test_id, status, duration, message)
        
        # TODO 1.11: "TC-001,PASS,1.2,Timeout after 30s" -> TestResult.
        #            Only the first two fields are required. The message may
        #            itself contain commas (hint: split with a limit).
        #            Strip spaces around each field. Too few fields -> ValueError.
       # raise NotImplementedError("TODO 1.11: from_csv_line")

    # ---- text forms ----------------------------------------------------------
    def __str__(self):
        result = f"{self.test_id} {self.status} {self.duration}s"
        
        if self.message:
            result += f" - {self.message}"
            
        return result
        # TODO 1.12: "TC-001 PASS 1.2s"  (add " - <message>" only if there is one)
        #raise NotImplementedError("TODO 1.12: __str__")

    def __repr__(self):
        return f"{type(self).__name__}({self.test_id!r}, {self.status!r}, {self.duration!r})"
        # TODO 1.12: "TestResult('TC-001', 'PASS', 1.2)"; use the REAL class name
        #            via type(self).__name__ so subclasses print correctly
        #raise NotImplementedError("TODO 1.12: __repr__")


class Suite:
    """A named collection of TestResult objects (has-a, not is-a list)."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Suite name must be non-empty text")
        
        self.name = name.strip()
        self._results = []
        
        # TODO 2.1: name must be non-empty text after strip() (else ValueError);
        #           store the stripped name in self.name
        # TODO 2.2: create the per-object list self._results here (NOT in the class body)
        #raise NotImplementedError("TODO 2.1-2.2: Suite.__init__")

    @classmethod
    def from_rows(cls, name, rows):
        suite = cls(name)
        for row in rows:
            result = TestResult.from_dict(row)
            suite.add(result)
        return suite
        # TODO 2.3: build a suite and add TestResult.from_dict(row) for every row
        #raise NotImplementedError("TODO 2.3: from_rows")

    def add(self, result):
        if not isinstance(result, TestResult):
            raise TypeError("Only TestResult objects can be added")
        for existing in self._results:
            if existing.test_id == result.test_id:
                raise ValueError(f"Duplicate test ID: {result.test_id}")
        self._results.append(result)
        # TODO 2.4: not a TestResult -> TypeError; a test_id already in the suite
        #           -> ValueError (mention the id); otherwise append
        #raise NotImplementedError("TODO 2.4: add")

    @property
    def results(self):
        return self._results.copy()
        # TODO 2.5: return a COPY of the internal list
        #raise NotImplementedError("TODO 2.5: results")

    def count(self):
        return len(self._results)
        # TODO 2.5: number of results
        #raise NotImplementedError("TODO 2.5: count")

    @property
    def pass_rate(self):
        if not self._results:
            return 0.0
        passed = sum(1 for result in self._results if result.status == "PASS")
        
        return(passed/len(self._results)) * 100
        # TODO 2.6: percent (0-100) of results whose status is PASS, out of ALL
        #           results (SKIPPED counts in the total). Empty suite -> 0.0
        #raise NotImplementedError("TODO 2.6: pass_rate")

    @property
    def total_duration(self):
        return sum(result.duration for result in self._results)
    
        # TODO 2.7: sum of all durations
        #raise NotImplementedError("TODO 2.7: total_duration")

    def counts_by_status(self):
        counts = {status: 0 for status in TestResult.VALID_STATUSES}
        
        for result in self._results:
            counts[result.status] += 1
        return counts
        # TODO 2.7: dict with EVERY valid status as a key, e.g.
        #           {"PASS": 2, "FAIL": 1, "SKIPPED": 1, "ERROR": 0}
        #raise NotImplementedError("TODO 2.7: counts_by_status")

    def failures(self):
        return [ result for result in self._results if result.status in ("FAIL", "ERROR")]
        
        # TODO 2.8: list of results whose status is FAIL or ERROR (suite order)
        #raise NotImplementedError("TODO 2.8: failures")

    def slowest(self, n=1):
        sorted_results = sorted( self._results, key=lambda result: result.duration, reverse=True)
        return sorted_results[:n]
        # TODO 2.8: the n slowest results, slowest first (sorted with a key)
        #raise NotImplementedError("TODO 2.8: slowest")


class Reporter:
    """Base class: presentation only. Subclasses override render()."""

    def __init__(self, suite):
        if not isinstance(suite, Suite):
            raise TypeError("Reporter requires a Suite object")
        
        self.suite = suite
        # TODO 3.1: suite must be a Suite (else TypeError); store it as self.suite
        #raise NotImplementedError("TODO 3.1: Reporter.__init__")

    @staticmethod
    def pad(text, width):
        return str(text).ljust(width)
        # TODO 3.2: str(text) left-justified in `width` characters. Never cut text.
        #raise NotImplementedError("TODO 3.2: pad")

    @staticmethod
    def format_percent(value):
        return f"{value:.1f}%"
        # TODO 3.2: 66.666 -> "66.7%"
        #raise NotImplementedError("TODO 3.2: format_percent")

    def render(self):
        raise NotImplementedError(f"{type(self).__name__} must implement render()")
        # TODO 3.3: the base class has no format: raise NotImplementedError with a
        #           helpful message naming the class (type(self).__name__)
        #pass

    def line_count(self):
        return len(self.render().splitlines())
        # TODO 3.4: number of lines in self.render(). Write it ONCE here;
        #           subclasses inherit it.
        #raise NotImplementedError("TODO 3.4: line_count")


class TextReporter(Reporter):
    def render(self):
        lines = [f"=== {self.suite.name} ==="]
        for result in self.suite.results:
            line = (self.pad(result.test_id, 8) + self.pad(result.status, 9) + f"{result.duration:5.1f}s")
            lines.append(line)

        lines.append(f"Pass rate: {self.format_percent(self.suite.pass_rate)}")

        return "\n".join(lines)
    
        # TODO 3.5: see README for the exact layout (header, one row per result,
        #           "Pass rate: 50.0%"). Use self.pad and self.format_percent.
        #raise NotImplementedError("TODO 3.5: TextReporter.render")


class CsvReporter(Reporter):
    HEADER = "test_id,status,duration,message"

    @staticmethod
    def clean_cell(text):
        return str(text).replace(",", ";").replace("\n", " ").replace("\r", " ")
        # TODO 3.6: commas -> ";" and newlines -> " " so one cell stays one cell
        #raise NotImplementedError("TODO 3.6: clean_cell")

    def render(self):
        lines = [self.HEADER]
        
        for result in self.suite.results:
            row = [
                self.clean_cell(result.test_id),
                self.clean_cell(result.status),
                str(result.duration),
                self.clean_cell(result.message)
            ]
            lines.append(",".join(row))

        return "\n".join(lines)
        # TODO 3.6: see README for the exact layout
        #raise NotImplementedError("TODO 3.6: CsvReporter.render")


# STRETCH 1: add class MarkdownReporter(Reporter) here (see README).