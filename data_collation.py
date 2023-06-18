#整理训练数据
def data_collation(df):
    selection1 = df['Data Validity Comment'].isna()
    selection2 = []
    for comment in df['Comment']:
        keep = True
        if comment and isinstance(comment, str) and comment.find('corresponding IC50 reported as Active') > 0: 
            keep = False
        selection2.append(keep)
    selection3 = df['Smiles'].notnull()
    df = df[selection1 & selection2 & selection3]
    
    active_selection = (df['Standard Relation']=="\'=\'") & (df['Standard Value'] < 1e4)
    active = df[active_selection]
    inactive = df[~active_selection]

    return active, inactive