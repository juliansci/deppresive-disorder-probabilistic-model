from problog.program import PrologFile
from problog.formula import LogicFormula
from problog import get_evaluatable

def main():
    program = PrologFile('model.txt')
    formula = LogicFormula.create_from(program)
    modelEvaluatable = get_evaluatable().create_from(formula)
    print modelEvaluatable.evaluate()
        
main()