import streamlit as st


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

ques = st.text_input('검색어를 입력해주세요.')
if ques:
    for ani, img in zip(ani_list, img_list):
        if ques in ani:
            st.image(img, width=300)


# text_input을 활용해서 검색창을 만듭니다.
# 이 검색창에 ani_list 안의 일부 단어가 일치하면 
# img_list의 해당 이미지를 출력하는 로직을 만들어 주세요.
# if / for 를 활용하면 될 겁니다.

# 화면에 뜨는 것부터 1개만 만들고 