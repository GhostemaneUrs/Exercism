class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        fila = 0
        for i in matrix_string.splitlines():
            self.matrix.append([])
            for j in i.split():
                self.matrix[fila].append(int(j))
            fila += 1

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        columna = []
        for fila in self.matrix:
            columna.append(fila[index - 1])
        return columna
