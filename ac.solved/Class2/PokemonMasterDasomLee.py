# 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
import sys

def solution():
    m, n = map(int, sys.stdin.readline().split())
    
    NumberPokemon = {}
    pokemonNumber = {}
    for i in range(1, m+1):
        pokemon = sys.stdin.readline().rstrip()
        pokemonNumber[pokemon] = i
        NumberPokemon[i] = pokemon
    
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        if line.isdigit():
            sys.stdout.write(NumberPokemon[int(line)] + '\n')
        else:
            sys.stdout.write(str(pokemonNumber[line]) + '\n')

solution()