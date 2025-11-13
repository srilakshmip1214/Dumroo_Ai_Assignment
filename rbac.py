def apply_scope(data, scope):
    result = data
    for key in ["grade", "class", "region"]:
        if key in data.columns:
            values = scope.get(key, [])
            if values:
                values = [str(v) for v in values]
                result = result[result[key].astype(str).isin(values)]
    return result
