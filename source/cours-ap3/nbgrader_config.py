c = get_config()
c.ClearSolutions.begin_solution_delimeter = "DEBUT DE MA SOLUTION"
c.ClearSolutions.end_solution_delimeter = "FIN DE MA SOLUTION"
c.ClearSolutions.code_stub = {
    "python": "# remplacer cette ligne par votre code\nraise NotImplementedError",
    "javascript": "// remplacer cette ligne par votre code\nthrow new Error();",
    "gp": "\\\\ remplacer cette ligne par votre code\nerror();"
}
