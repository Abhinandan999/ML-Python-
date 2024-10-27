//This problem requires us to return the first 3 rows of the employees DataFrame.

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
    
