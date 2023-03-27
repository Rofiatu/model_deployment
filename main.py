import streamlit as st
from PIL import Image
st.title('Welcome to BMI calculator')
user_name = st.text_input('Enter your name', 'Type your name')

# create a button that displays a welcome message

if(st.button('Please click me for your welcome message')):
    st.text(f'Welcome to GoMyCode, {user_name}!')

# # request to know gender

# gender = st.radio('What is your gender?: ', ('Male', 'Female'))

# instantiate weight

weight = st.number_input('Enter your weight (in kgs)')

# instantiate the metric

metric = st.radio('Select your height format: ', ('Centimeters','Meters','Feet'))

# create a loop for each metric measurement

try:
    if(metric == 'cms'):
        height = st.number_input('Centimeters')
        bmi = weight / ((height/100)**2)

    elif(metric == 'meters'):
        height = st.number_input('Meters')
        bmi = weight / (height ** 2)

    else:
        height = st.number_input('Feet')
        bmi = weight / (((height/3.28))**2)

# return the result of the calculation

    st.text(f'Your BMI is {bmi}')

# create conditionals for interpreting the BMI

    if(bmi < 16):
        result = st.error('You are extremely underweight')
        extreme_underweight = 'https://images.everydayhealth.com/images/diet-nutrition/weight/bmi-in-adults-722x406.jpg'
        st.image(extreme_underweight, caption = 'BMI weight chart', width = 400)
        st.text('''Being underweight has the following associated risks: \n
1. Malnutrition, vitamin deficiencies, anemia (lowered ability to carry blood vessels) \n
2. Osteoporosis, a disease that causes bone weakness, increasing the risk of breaking a bone \n
3. A decrease in immune function \n
4. Growth and development issues, particularly in children and teenagers \n
5. Possible reproductive issues for women due to hormonal imbalances that can disrupt the menstrual cycle. Underweight women also have a higher chance of miscarriage in the first trimester \n
6. Potential complications as a result of surgery \n
Generally, an increased risk of mortality compared to those with a healthy BMI
In some cases, being underweight can be a sign of some underlying condition or disease such as anorexia nervosa, which has its own risks. Consult your doctor if you think you or someone you know is underweight, particularly if the reason for being underweight does not seem obvious.
        ''')
    elif(bmi >= 16 and bmi < 18.5):
        result = st.warning('You are underweight')
        underweight = 'https://images.everydayhealth.com/images/diet-nutrition/weight/bmi-in-adults-722x406.jpg'
        st.image(underweight, caption='BMI weight chart', width=400)
        st.text('''Being underweight has the following associated risks, listed below: \n
1. Malnutrition, vitamin deficiencies, anemia (lowered ability to carry blood vessels) \n
2. Osteoporosis, a disease that causes bone weakness, increasing the risk of breaking a bone \n
3. A decrease in immune function \n
4. Growth and development issues, particularly in children and teenagers \n
5. Possible reproductive issues for women due to hormonal imbalances that can disrupt the menstrual cycle. Underweight women also have a higher chance of miscarriage in the first trimester \n
6. Potential complications as a result of surgery \n
Generally, an increased risk of mortality compared to those with a healthy BMI
In some cases, being underweight can be a sign of some underlying condition or disease such as anorexia nervosa, which has its own risks. Consult your doctor if you think you or someone you know is underweight, particularly if the reason for being underweight does not seem obvious. \n
Source: https://www.calculator.net/bmi-calculator.html?ctype=standard&cage=25&csex=m&cheightfeet=5&cheightinch=10&cpound=160&cheightmeter=180&ckg=65&printit=0&x=71&y=18
        ''')
    elif(bmi >= 18.5 and bmi < 25):
        result = st.success('Healthy weight')
        healthy = 'https://images.everydayhealth.com/images/diet-nutrition/weight/bmi-in-adults-722x406.jpg'
        st.image(healthy, caption='BMI weight chart', width=400)
        st.text(''' The following are the benefits of a healthy BMI: \n
1. Reduced risk of Covid-19 complications \n
2. Reduced risk of type 2 diabetes \n
3. Reduced risk of cardiovascular disease and heart attacks \n
4. Fewer joint and muscle problems \n
5. Improved fertility \n
6. Better mobility and self-confidence \n

In order to maintain a healthy BMI, you may do the following: \n
1. Eat a balanced calorie-controlled diet \n
2. Reduce sugar intake \n
3. Exercise your heart regularly \n
4. Move more \n

Source: https://www.livi.co.uk/your-health/5-simple-tips-for-a-healthy-bmi/
        ''')
    elif(bmi >= 25 and bmi < 30):
        result = st.warning('Overweight')
        overweight = 'https://images.everydayhealth.com/images/diet-nutrition/weight/bmi-in-adults-722x406.jpg'
        st.image(overweight, caption='BMI weight chart', width=400)
        st.text(''' Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks, according to the Centers for Disease Control and Prevention (CDC): \n
1. High blood pressure \n
2. Higher levels of LDL cholesterol, which is widely considered "bad cholesterol," lower levels of HDL cholesterol, considered to be good cholesterol in moderation, and high levels of triglycerides \n
3. Type II diabetes \n
4. Coronary heart disease \n
5. Stroke \n
6. Gallbladder disease \n
7. Osteoarthritis, a type of joint disease caused by breakdown of joint cartilage \n
8. Sleep apnea and breathing problems \n
9. Certain cancers (endometrial, breast, colon, kidney, gallbladder, liver) \n
10. Low quality of life \n
11. Mental illnesses such as clinical depression, anxiety, and others \n
12. Body pains and difficulty with certain physical functions \n
Generally, an increased risk of mortality compared to those with a healthy BMI
As can be seen from the list above, there are numerous negative, in some cases fatal, outcomes that may result from being overweight. Generally, a person should try to maintain a BMI below 25 kg/m2, but ideally should consult their doctor to determine whether or not they need to make any changes to their lifestyle in order to be healthier.
Source: https://www.calculator.net/bmi-calculator.html?ctype=standard&cage=25&csex=m&cheightfeet=5&cheightinch=10&cpound=160&cheightmeter=180&ckg=65&printit=0&x=71&y=18   
        ''')
    elif(bmi >= 30):
        result = st.error('Extremely overweight')
        extreme_overweight = 'https://images.everydayhealth.com/images/diet-nutrition/weight/bmi-in-adults-722x406.jpg'
        st.image(extreme_overweight, caption='BMI weight chart', width = 400)
        st.text(''' Being overweight increases the risk of a number of serious diseases and health conditions. Below is a list of said risks, according to the Centers for Disease Control and Prevention (CDC): \n
1. High blood pressure \n
2. Higher levels of LDL cholesterol, which is widely considered "bad cholesterol," lower levels of HDL cholesterol, considered to be good cholesterol in moderation, and high levels of triglycerides \n
3. Type II diabetes \n
4. Coronary heart disease \n
5. Stroke \n
6. Gallbladder disease \n
7. Osteoarthritis, a type of joint disease caused by breakdown of joint cartilage \n
8. Sleep apnea and breathing problems \n
9. Certain cancers (endometrial, breast, colon, kidney, gallbladder, liver) \n
10. Low quality of life \n
11. Mental illnesses such as clinical depression, anxiety, and others \n
12. Body pains and difficulty with certain physical functions \n
Generally, an increased risk of mortality compared to those with a healthy BMI
As can be seen from the list above, there are numerous negative, in some cases fatal, outcomes that may result from being overweight. Generally, a person should try to maintain a BMI below 25 kg/m2, but ideally should consult their doctor to determine whether or not they need to make any changes to their lifestyle in order to be healthier.
Source: https://www.calculator.net/bmi-calculator.html?ctype=standard&cage=25&csex=m&cheightfeet=5&cheightinch=10&cpound=160&cheightmeter=180&ckg=65&printit=0&x=71&y=18   
        ''')
     
except:
    st.text('There seems to be an error hindering the ability to render an accurate BMI report. Please try again shortly.')
