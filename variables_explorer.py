import streamlit as st

# 设置页面标题和图标
st.set_page_config(page_title="变量探险家", page_icon=":compass:")

# --- 游戏状态管理 ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_num' not in st.session_state:
    st.session_state.question_num = 1
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'user_answer' not in st.session_state:
    st.session_state.user_answer = ''

# --- 问题数据 ---
questions = {
    1: {"text": "以下哪个不是有效的 Python 变量名？", "options": ["my_variable", "123variable", "_variable", "variable123"], "answer": "B", "explanation": "变量名不能以数字开头。"},
    2: {"text": "在 Python 中，用于存储文本信息的数据类型是什么？", "options": ["int", "float", "str", "bool"], "answer": "C", "explanation": "str 代表字符串 (string)，用于存储文本。"},
    3: {"text": "以下哪个 Python 代码可以创建一个名为 age，值为 20 的变量？", "options": ["age = '20'", "age = 20.0", "age = 20", "age = int('20')"], "answer": ["C", "D"], "explanation": "C 选项直接赋值整数；D 选项先将字符串 '20' 转换为整数再赋值。"},
    4: {"text": "假设 name = '小明'，age = 18，以下哪段代码可以输出 '我叫小明，今年18岁。'？", "options": ["print('我叫' + name + '，今年' + age + '岁。')", "print(f'我叫{name}，今年{age}岁。')", "print('我叫 %s，今年 %d 岁。' % (name, age))", "print('我叫 {0}，今年 {1} 岁。'.format(name, age))"], "answer": "B", "explanation": "f-string 提供了一种更简洁的方式来格式化字符串，使用大括号 {} 嵌入变量。"},
    5: {"text": "想要获得用户输入的信息，应该使用哪个函数？", "options": ["print()", "type()", "input()", "str()"], "answer": "C", "explanation": "input() 函数可以让用户输入信息。"},
    6: {"text": "以下代码的输出结果是什么？\nx = 10\ny = 3\nprint(x / y)", "options": ["3", "3.33", "3.3333333333333335", "10/3"], "answer": "C", "explanation": "在 Python 中，`/` 运算符执行的是浮点数除法。"},
    7: {"text": "以下代码的输出结果是什么？\nx = 10\ny = 3\nprint(x // y)", "options": ["3", "3.33", "3.3333333333333335", "10//3"], "answer": "A", "explanation": "在 Python 中，`//` 运算符执行的是整除，结果向下取整。"},
    8: {"text": "以下哪个函数可以用来查看变量的类型？", "options": ["input()", "print()", "type()", "str()"], "answer": "C", "explanation": "`type()`可以用来查看变量的类型。"},
    9: {"text": "如何将整数10, 转成字符串'10'?", "options": ["int('10')", "float(10)", "str(10)", "bool(10)"], "answer": "C", "explanation": "`str()`可以将整数转成字符串。"},
    10: {"text": "以下代码的输出结果是什么？\nmessage = 'Hello, World!'\nprint(len(message))", "options": ["Hello", "World", "12", "13"], "answer": "D", "explanation": "`len()` 函数返回字符串的长度（包括空格和标点符号）。"}
}

# --- CSS 样式（用于隐藏 radio 选项）---
st.markdown("""
<style>
.hide-radio .stRadio > div > div {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# --- 游戏主界面 ---
st.title("变量探险家 :compass:")
st.write("你将通过回答一系列关于变量和数据类型的问题来收集宝藏。")

if st.session_state.question_num <= len(questions):
    st.header(f"问题 {st.session_state.question_num}/{len(questions)}")
    question = questions[st.session_state.question_num]
    st.write(question["text"])

    # 使用 radio 组件显示选项
    temp_answer = st.radio("请选择你的答案：",
                        options=[f"{opt}" for opt in question["options"]],
                        key=f"question_{st.session_state.question_num}",
                        label_visibility="visible" if not st.session_state.answered else "collapsed"
                        )
    # 根据 answered 状态添加 CSS 类
    if st.session_state.answered:
        st.markdown(f'<style>.stRadio {{display: none;}}</style>', unsafe_allow_html=True)


    if st.button("提交答案", key=f"submit_{st.session_state.question_num}", disabled=st.session_state.answered):
        st.session_state.answered = True
        st.session_state.user_answer = temp_answer[0]  # 从临时变量获取选择

        if isinstance(question["answer"], list):
            correct_answers = question["answer"]
            if st.session_state.user_answer in correct_answers:
                st.success("恭喜你答对了！你获得了 10 个变量币！")
                st.session_state.score += 10
            else:
                st.error("很遗憾，答错了。")
        elif st.session_state.user_answer == question["answer"]:
            st.success("恭喜你答对了！你获得了 10 个变量币！")
            st.session_state.score += 10
        else:
            st.error("很遗憾，答错了。")
        st.session_state.show_answer = True
        st.rerun()

    if st.session_state.show_answer:
        st.info(f"正确答案是：{', '.join(question['answer']) if isinstance(question['answer'], list) else question['answer']}")
        st.write(f"解释：{question['explanation']}")
        if st.button("下一题", key=f"next_{st.session_state.question_num}"):
            st.session_state.question_num += 1
            st.session_state.answered = False
            st.session_state.show_answer = False
            st.session_state.user_answer = ''
            st.rerun()

else:
    st.header("游戏结束！")
    st.write(f"你总共获得了 {st.session_state.score} 个变量币！")
    st.balloons()
    if st.button("重新开始"):
        st.session_state.score = 0
        st.session_state.question_num = 1
        st.session_state.answered = False
        st.session_state.show_answer = False
        st.session_state.user_answer = ''
        st.rerun()