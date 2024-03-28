# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") # 외부 텍스트 데이터 -> 데이터 프레임으로 변환해서 반환 
    return df

def plot_matplotlib():
    st.title("Bar Plot") # 그래프 제목 Bar Plot(막대 그래프)
    df = load_data() # 데이터 준비 
    # 그래프 그리기 
    fig, ax = plt.subplots()
    
    # 막대그래프 
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("Year vs. lifeExp") #18 ~ 24 는 파이썬에 제공해주는 막대그래프 툴? 디자인? 맞으려나 ~ 
    # 웹 OR 앱 에 시각화를 하려면 st.pyplot(fig) 활용해서 위에서 정의한 이걸 보여줘야한다.
    
    st.pyplot(fig)

def main():
    st.title("데이터 시각화 : 표 & 그래프")
    
    df = load_data() # 데이터 불로오기 : 데이터 프레임  [df는 데이터 프레임(data frame)]
    st.dataframe(df, use_container_width=True) # 첫번째 표 

    #pandas style #두번째 표 
    st.title("컬럼별 최대값 표")
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib() #그래프 
    
    
if __name__ == "__main__":
    main()