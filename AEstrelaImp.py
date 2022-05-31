# Nome: Guilherme José Bitencourt Lopes
# Matricula: 95660

from numpy import Infinity
from Posicao import Posicao
from AEstrela import AEstrela
from QuebraCabeca import QuebraCabeca
from QuebraCabecaImp import QuebraCabecaImp
import heapq as hq


class AEstrelaImp(AEstrela):
    def getSolucao(self, qc):
        qCopy = QuebraCabecaImp() 
        qCopy.setTab(qc.getTab())
        start = qCopy.hashCode()
        startPos = qCopy.getTab()
        #openStates = [start]
        openStates = [(qCopy.getValor(), start)]
        hq.heapify(openStates)
        g = {start : 0}

        f = {start : qCopy.getValor()}

        hash = {start : startPos}

        map = {}

        while len(openStates) > 0:
            temp = hq.heappop(openStates)
            current = temp[1]

            '''
            min = Infinity
            current = 0
            for i in openStates:
                if f[i] < min:
                    min = f[i]
                    current = i
            '''

            qCopy.setTab(hash[current])
            if qCopy.isOrdenado():
                path = [Posicao(qCopy.getPosVazio().getLinha(), qCopy.getPosVazio().getColuna())]
                while current in map:
                    current = map[current]
                    qCopy.setTab(hash[current])
                    #print(qCopy.getTab()[0])
                    #print(qCopy.getTab()[1])
                    #print(qCopy.getTab()[2])
                    #print(" ")
                    path.insert(0, Posicao(qCopy.getPosVazio().getLinha(), qCopy.getPosVazio().getColuna()))
                return path

            for m in qCopy.getMovePossiveis():
                qCopy.move(qCopy.getPosVazio().getLinha(),qCopy.getPosVazio().getColuna(),m.getLinha(), m.getColuna())
                nextState = qCopy.hashCode()
                score = g[current] + 1 #todos os movimentos tem peso 1 neste quebra cabeça
                if nextState not in g:
                     g[nextState] = Infinity
                if (score < g[nextState]):
                    map[nextState] = current
                    g[nextState] = score
                    f[nextState] = score + qCopy.getValor()
                    hash[nextState] = qCopy.getTab()
                    if qCopy.hashCode() not in [k for v, k in openStates]:
                        hq.heappush(openStates, (qCopy.getValor(), qCopy.hashCode()))
                    
                    #print(score)
                qCopy.setTab(hash[current])
        return []
