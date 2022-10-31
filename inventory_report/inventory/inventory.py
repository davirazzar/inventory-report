import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        """Reads a file from a given path and returns its contents
        Parameters
        ----------
        path : str
            Full path to file
        type : str
            If its going to generate a Simple or Completed report
        Returns
        -------
        list
            List of rows as dicts
        """
        with open(path, encoding="utf-8") as file:
            reports = list(csv.DictReader(file, delimiter=",", quotechar='"'))
            result = []
            if type == "simples":
                result = SimpleReport().generate(reports)
            elif type == "completo":
                result = CompleteReport().generate(reports)
        return result
