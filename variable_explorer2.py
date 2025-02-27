import streamlit as st

# 设置页面标题和布局
st.set_page_config(page_title="变量探险家 - Python 变量与数据类型小游戏", layout="wide")

# --- 游戏初始化 ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'question_num' not in st.session_state:
    st.session_state.question_num = 0
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {
            "text": "以下哪个不是有效的 Python 变量名？",
            "options": ["A. my_variable", "B. 123variable", "C. _variable", "D. variable123"],
            "answer": "B",
            "explanation": "变量名不能以数字开头。"
        },
        {
            "text": "在 Python 中，用于存储文本信息的数据类型是什么？",
            "options": ["A. int", "B. float", "C. str", "D. bool"],
            "answer": "C",
            "explanation": "str 代表字符串 (string)，用于存储文本。"
        },
        {
            "text": "以下哪个 Python 代码可以创建一个名为 age，值为 20 的变量？",
            "options": ["A. age = '20'", "B. age = 20.0", "C. age = 20", "D. age = int('20')"],
            "answer": ("C", "D"),
            "explanation": "C选项直接赋值整数；D选项先将文字'20'转换为整数再赋值。"
        },
        {
            "text": "假设 name = '小明'，age = 18，以下哪段代码可以输出 '我叫小明，今年18岁。'？",
            "options": ["A. print('我叫' + name + '，今年' + age + '岁。')", "B. print(f'我叫{name}，今年{age}岁。')",
                                 "C. print('我叫 %s，今年 %d 岁。' % (name, age))",
                                 "D. print('我叫 {0}，今年 {1} 岁。'.format(name, age))"],
            "answer": "B",
            "explanation": "f-string 提供了一种更简洁的方式来格式化字符串，使用大括号 {} 嵌入变量。"
        },
        {
            "text": "想要获得使用者输入的信息，应该使用哪个函数?",
            "options": ["A. print()", "B. type()", "C. input()", "D. str()"],
            "answer": "C",
            "explanation": "input()函数可以让使用者输入信息。"
        },
        {
            "text": "以下哪个选项可以将一个字符串 '3.14' 转换为浮点数？",
            "options": ["A. int('3.14')", "B. float('3.14')", "C. str(3.14)", "D. bool('3.14')"],
            "answer": "B",
            "explanation": "float() 函数可以将字符串或整数转换为浮点数。"
        },
        {
            "text": "在 Python 中，表示“真”的布尔值是什么？",
            "options": ["A. 0", "B. 1", "C. False", "D. True"],
            "answer": "D",
            "explanation": "True 表示逻辑真，False 表示逻辑假。"
        },
        {
            "text": "以下哪个运算符用于计算两个数的商（结果为浮点数）？",
            "options": ["A. +", "B. -", "C. *", "D. /"],
            "answer": "D",
            "explanation": "// 运算符执行除法运算，结果始终为浮点数。"
        },
        {
            "text": "如果 a = 10，b = 3，那么 a // b 的结果是什么？",
            "options": ["A. 3.333...", "B. 3", "C. 1", "D. 7"],
            "answer": "B",
            "explanation": "// 运算符执行整除运算，结果为商的整数部分。"
        },
        {
            "text": "如果 a = 5，b = 2，那么 a ** b 的结果是什么？",
            "options": ["A. 7", "B. 10", "C. 25", "D. 3"],
            "answer": "C",
            "explanation": "** 运算符执行幂运算，a ** b 表示 a 的 b 次方。"
        },
        {
            "text": "以下哪个函数可以查看变量的数据类型？",
            "options": ["A. input()", "B. print()", "C. type()", "D. len()"],
            "answer": "C",
            "explanation": "type() 函数可以返回变量的数据类型。"
        },
        {
            "text": "以下哪个是 Python 中的注释符号？",
            "options": ["A. //", "B. /* */", "C. #", "D. --"],
            "answer": "C",
            "explanation": "# 符号用于单行注释，其后的内容会被 Python 解释器忽略。"
        },
        {
            "text": "在 f-string 中，如果要在字符串中显示大括号 {} 本身，应该怎么做？",
            "options": ["A. \{ \}", "B. {{ }}", "C. { }", "D. \\{ \\}"],
            "answer": "B",
            "explanation": "使用双大括号 {{ }} 来表示一个大括号字符。"
        },
        {
            "text": "如果要将一个整数 10 转换为字符串，应该使用哪个函数？",
            "options": ["A. int()", "B. float()", "C. str()", "D. bool()"],
            "answer": "C",
            "explanation": "str() 函数可以将其他数据类型转换为字符串。"
        },
        {
            "text": "以下哪个是正确的 f-string 格式化，用于将数字 3.14159 保留两位小数？",
            "options": ["A. f'{3.14159:d}'", "B. f'{3.14159:s}'", "C. f'{3.14159:.2f}'", "D. f'{3.14159:2'"],
            "answer": "C",
            "explanation": ":.2f 指定了浮点数的格式，保留两位小数。"
        }

    ]

# --- 游戏主界面 ---

# 游戏标题
st.title("变量探险家")
st.write("欢迎来到《变量探险家》！你将通过回答关于变量和数据类型的问题来收集变量币，成为变量大师！")

# 显示当前得分
st.write(f"当前得分：**{st.session_state.score}** 变量币")

# 检查是否还有问题
if st.session_state.question_num < len(st.session_state.questions):
    question = st.session_state.questions[st.session_state.question_num]

    st.write("---")
    # 显示问题
    st.subheader(f"问题 {st.session_state.question_num + 1}:")
    st.write(question["text"])

    # 显示选项, 使用 radio 组件
    user_answer = st.radio("请选择你的答案：", question["options"], key=f"question_{st.session_state.question_num}")


    # 提交按钮
    if st.button("提交", key=f"submit_{st.session_state.question_num}"):
        # 检查答案
        correct = False
        if isinstance(question["answer"], tuple):  # 多选答案
             if user_answer[0] in question["answer"]:
                  correct = True
        elif user_answer[0] == question["answer"]:
            correct = True

        # 显示结果
        if correct:
            st.success("回答正确！你获得了一些变量币！")
            st.session_state.score += 10  # 答对一题得 10 分
        else:
            st.error(f"回答错误。正确答案是 {question['answer']}。")
        st.write(f"解释：{question['explanation']}")

        # 更新问题编号
        st.session_state.question_num += 1

        # 强制刷新
        st.rerun()

else:
    # 所有问题都已回答完毕
    st.balloons()
    st.success(f"恭喜你完成了所有挑战！你的最终得分是：{st.session_state.score} 变量币。你已经成为了一名合格的变量大师！")

    # 重置游戏按钮
    if st.button("重新开始"):
        st.session_state.question_num = 0
        st.session_state.score = 0
        st.rerun()