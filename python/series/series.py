def slices(series, length):
    result = []
    if length > 0 and length <= len(series):

        for i in range(len(series) - length + 1):
            result.append(series[i:i+length])
        return result
    else:
        raise ValueError("Los valores introducidos no son validos")
