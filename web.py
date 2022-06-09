import requests
import streamlit as st
from streamlit_lottie import st_lottie

from distutils.log import error
from lib2to3.pgen2 import token
from pickle import FALSE
import string
from symtable import Symbol

def LexicalAnalyzer(kata):

    input_kata = kata.lower() + '#'
    tabel_transisi ={}


    #q0
    tabel_transisi[('q0', ' ')] = 'q0'

    # syahde
    tabel_transisi[('q0', 's')] = 'q1'
    tabel_transisi[('q1', 'y')] = 'q2'
    tabel_transisi[('q2', 'a')] = 'q3'
    tabel_transisi[('q3', 'h')] = 'q4'
    tabel_transisi[('q4', 'd')] = 'q23'
    tabel_transisi[('q23', 'e')] = 'q44'

    # henzi
    tabel_transisi[('q0','h')] = 'q6'
    tabel_transisi[('q6','e')] = 'q7'
    tabel_transisi[('q7','n')] = 'q8'
    tabel_transisi[('q8','z')] = 'q9'
    tabel_transisi[('q9','i')] = 'q44'

    # yasmin
    tabel_transisi[('q0','y')] = 'q10'
    tabel_transisi[('q10','a')] = 'q11'
    tabel_transisi[('q11','s')] = 'q12'
    tabel_transisi[('q12','m')] = 'q13'
    tabel_transisi[('q13','i')] = 'q14'
    tabel_transisi[('q14','n')] = 'q44'

    # pizza
    tabel_transisi[('q0','p')] = 'q15'
    tabel_transisi[('q15','i')] = 'q16'
    tabel_transisi[('q16','z')] = 'q17'
    tabel_transisi[('q17','z')] = 'q18'
    tabel_transisi[('q18','a')] = 'q44'

    # coffee
    tabel_transisi[('q0','c')] = 'q19'
    tabel_transisi[('q19','o')] = 'q20'
    tabel_transisi[('q20','f')] = 'q21'
    tabel_transisi[('q21','f')] = 'q22'
    tabel_transisi[('q22','e')] = 'q23'
    tabel_transisi[('q23','e')] = 'q44'

    # movie
    tabel_transisi[('q0','m')] = 'q24'
    tabel_transisi[('q24','o')] = 'q25'
    tabel_transisi[('q25','v')] = 'q26'
    tabel_transisi[('q26','i')] = 'q23'
    tabel_transisi[('q23','e')] = 'q44'

    # medicine
    tabel_transisi[('q0','m')] = 'q24'
    tabel_transisi[('q24','e')] = 'q27'
    tabel_transisi[('q27','d')] = 'q28'
    tabel_transisi[('q28','i')] = 'q29'
    tabel_transisi[('q29','c')] = 'q30'
    tabel_transisi[('q30','i')] = 'q31'
    tabel_transisi[('q31','n')] = 'q23'
    tabel_transisi[('q23','e')] = 'q44'

    # eats
    tabel_transisi[('q0','e')] = 'q32'
    tabel_transisi[('q32','a')] = 'q33'
    tabel_transisi[('q33','t')] = 'q34'
    tabel_transisi[('q34','s')] = 'q44'

    # drinks
    tabel_transisi[('q0','d')] = 'q35'
    tabel_transisi[('q35','r')] = 'q36'
    tabel_transisi[('q36','i')] = 'q37'
    tabel_transisi[('q37','n')] = 'q38'
    tabel_transisi[('q38','k')] = 'q34'
    tabel_transisi[('q34','s')] = 'q44'

    # watch
    tabel_transisi[('q0','w')] = 'q39'
    tabel_transisi[('q39','a')] = 'q40'
    tabel_transisi[('q40','t')] = 'q41'
    tabel_transisi[('q41','c')] = 'q42'
    tabel_transisi[('q42','h')] = 'q43'
    tabel_transisi[('q43','e')] = 'q34'
    tabel_transisi[('q34','s')] = 'q44'

    # New token
    tabel_transisi[('q45', 's')] = 'q1'
    tabel_transisi[('q45', 'h')] = 'q6'
    tabel_transisi[('q45', 'y')] = 'q10'
    tabel_transisi[('q45', 'p')] = 'q15'
    tabel_transisi[('q45', 'c')] = 'q19'
    tabel_transisi[('q45', 'm')] = 'q24'
    tabel_transisi[('q45', 'e')] = 'q32'
    tabel_transisi[('q45', 'd')] = 'q35'
    tabel_transisi[('q45', 'w')] = 'q39'

    # Final state
    tabel_transisi[('q44', ' ')] = 'q45'
    tabel_transisi[('q44', '#')] = 'accept'
    tabel_transisi[('q45', '#')] = 'accept'
    tabel_transisi[('q45', ' ')] = '45'


    # Main Program #
    current_token = ''
    state = 'q0'
    n = 0

    while state != 'accept':
        huruf = input_kata[n]
        current_token += huruf

        try:
            state = tabel_transisi[(state, huruf)]
        except:
            state = None

        if state == 'q44':
            current_token = ''
        elif state == None:
            break

        n += 1

    if state == 'accept':
        #st.write('Semua kata telah dianalisis : ',kata,' -> valid')
        valid = True
        return valid

    elif state == None:
        #st.write('Semua kata telah dianalisis : ',kata,' -> tidak valid')
        valid = False
        return valid


def parser(kalimat):
    non_terminal = ['S', 'V', 'N']
    terminal = ['syahde', 'henzi', 'yasmin', 'eats', 'drinks', 'watches', 'pizza', 'coffee', 'movie', 'medicine']

    stack = []
    stack.append('#')
    stack.append('S')

    tokens = kalimat.lower().split()
    tokens.append('EOS')

    # Tabel Parser #
    parse_table = {}

    # EOS
    parse_table[('S','EOS')] = ['error']
    parse_table[('N','EOS')] = ['error']
    parse_table[('V','EOS')] = ['error']

    # S
    parse_table[('S','syahde')] = ['N', 'V', 'N']
    parse_table[('S','henzi')] = ['N', 'V', 'N']
    parse_table[('S','yasmin')] = ['N', 'V', 'N']
    parse_table[('S','eats')] = ['error']
    parse_table[('S','drinks')] = ['error']
    parse_table[('S','watches')] = ['error']
    parse_table[('S','pizza')] = ['N', 'V', 'N']
    parse_table[('S','coffee')] = ['N', 'V', 'N']
    parse_table[('S','movie')] = ['N', 'V', 'N']
    parse_table[('S','medicine')] = ['N', 'V', 'N']

    # N
    parse_table[('N','syahde')] = ['syahde']
    parse_table[('N','henzi')] = ['henzi']
    parse_table[('N','yasmin')] = ['yasmin']
    parse_table[('N','eats')] = ['error']
    parse_table[('N','drinks')] = ['error']
    parse_table[('N','watches')] = ['error']
    parse_table[('N','pizza')] = ['pizza']
    parse_table[('N','coffee')] = ['coffee']
    parse_table[('N','movie')] = ['movie']
    parse_table[('N','medicine')] = ['medicine']

    # V
    parse_table[('V','syahde')] = ['error']
    parse_table[('V','henzi')] = ['error']
    parse_table[('V','yasmin')] = ['error']
    parse_table[('V','eats')] = ['eats']
    parse_table[('V','drinks')] = ['drinks']
    parse_table[('V','watches')] = ['watches']
    parse_table[('V','pizza')] = ['error']
    parse_table[('V','coffee')] = ['error']
    parse_table[('V','movie')] = ['error']
    parse_table[('V','medicine')] = ['error']

    if valid == True:
        idx_token = 0
        simbol = tokens[idx_token]

        while (len(stack) > 0 ):
            top = stack[len(stack)-1]

            if top in terminal:

                if top==simbol:
                    stack.pop()
                    idx_token = idx_token + 1
                    simbol = tokens[idx_token]

                    if simbol == 'EOS':
                        stack.pop()

                else:
                    #print("GRAMMAR ERROR")
                    break

            elif top in non_terminal:

                if parse_table[(top,simbol)][0] != error:
                    stack.pop()
                    simbol_to_be_pushed = parse_table[(top, simbol)]

                    for i in range(len(simbol_to_be_pushed)-1, -1, -1):
                        stack.append(simbol_to_be_pushed[i])

                else:
                    #print("GRAMMAR ERROR")
                    break
            else:
                #print("GRAMMAR ERROR")
                break

        if (simbol == 'EOS') and (len(stack) == 0):
            st.write("Verified : '",kalimat, "' terdapat dalam list :white_check_mark: ")
            st.write("Kalimat : '", kalimat, "' diterima oleh grammar :white_check_mark: ")
        else:
            st.write("Verified : '",kalimat, "' terdapat dalam list :white_check_mark:")
            st.write("Kalimat : '", kalimat, "' tidak diterima oleh grammar :x: ")

# Proses Front End Website #
st.set_page_config(page_title="TUBES TBA", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dianq89m.json")

automata = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_jwvsfeti.json")

# HEADER JUDUL #
with st.container():
    st.subheader("Haloo User :wave: ")
    st.title("PROGRAM LEXICAL ANALYZER & PARSER SEDERHANA")
    st_lottie(animation, height=500, key="coding")


# LIST KATA #
with st.container():
    st.write("---")
    left,mid, right = st.columns(3)

    with mid:
        st.title("LIST KATA")
    
    st.write("---")

# SVO #
with st.container():
    left, mid, right = st.columns(3)

    with left:
        st.header("Subject")
        st.header("(S)")
        st.write("Yasmin")
        st.write("Henzi")
        st.write("Syahde")
    
    with mid:
        st.header("Verb")
        st.header("(V)")
        st.write("Eats")
        st.write("Drinks")
        st.write("Watches")

    with right:
        st.header("Object")
        st.header("(O)")
        st.write("Coffee")
        st.write("Medicine")
        st.write("Movie")
        st.write("Pizza")
    
    st.write("---")
    st.subheader("Accepted Sentence : S/O + V + S/O")
    st.write("---")

# INPUT #
with st.container():
    left, mid, right = st.columns(3)

    with mid:
        st.title("INPUT & HASIL")
    st.write("---")

# MASUKKAN KALIMAT #
with st.container():
    left, right = st.columns(2)

    with left:
        st_lottie(automata, height=300, key="process")

    with right:
        st.header("Masukkan kalimat")
        kalimat = st.text_input("")

        if kalimat != "":
            valid = LexicalAnalyzer(kalimat)
 
            if valid == True:
                parser(kalimat)
            elif valid == False:
                st.write("Error : '", kalimat, "' tidak terdapat dalam list :x:")
                st.write("Kalimat : '", kalimat, "' tidak sesuai dengan grammar :x:")
    st.write("---")

# MADE BY #
with st.container():
    left, mid, right = st.columns(3)
    
    with mid :
        st.title("MADE BY")
    #st.write("---")
    


# NAMA #
with st.container():
    left, mid, right = st.columns(3)

    with left:
        st.header("AISYAH DLIYA RAMADHANTI")
        st.subheader("(1301201154)")
    
    with mid:
        st.header("HENZI JUANDRI")
        st.subheader("(1301202285)")

    with right:
        st.header("FIJAR YASMINA PRITAMA")
        st.subheader("(1301200215)")

    st.write("---")

    



    


    
        

    