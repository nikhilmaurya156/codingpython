from flask import Flask, render_template, url_for, request
import re
import random
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('1st_page.html', title='Home')


@app.route('/result', methods=['POST'])
def result():
    dat = request.form['date']
    d_o_b = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
    mo = d_o_b.search(str(dat))

    if mo == None:
        return render_template('1st_page.html', title='Home', error='Enter in a valid Format')
    else:
        horoscope = ['ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO', 'LIBRA', 'SCORPION', 'SAGITTARIUS',
                     'CAPRICORN', 'AQUARIUS', 'PISCES']
        b = []
        dob = mo.group()
        date = int(mo.group(1))
        mont = str(mo.group(2))
        if (mont == '04' and date <= 20) or (mont == '03' and (21 <= date <= 31)):
            c = horoscope[0]
            strengths = ['Courage', 'Determination', 'self-confidence', 'enthusiasm']
            weakness = ['Impatience', 'Silly Arguments', 'Fear To limit Choices']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '05' and date <= 21) or (mont == '04' and (21 <= date <= 30)):
            c = horoscope[1]
            strengths = ['Dependable', 'Patient', 'Musical', 'Practical']
            weakness = ['Stubborn', 'Upcoming', 'Possessive']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '06' and date <= 21) or (mont == '05' and (21 <= date <= 31)):
            c = horoscope[2]
            strengths = ['Curiosity', 'Ability To Share Ideas', 'Adaptable', 'Affectionate', 'Kind']
            weakness = ['fickle in Love', 'nervous', 'Short Attention Span' ]
            return render_template('result.html', title='Result', sign=c, dob=dob,  stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '07' and date <= 22) or (mont == '06' and (22 <= date <= 30)):
            c = horoscope[3]
            strengths = ['Compassion', 'Emotional Sensitivity', 'Tenacity']
            weakness = ['Manipulative', 'Indirect Conflict', 'Insecure', 'Packrat']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '08' and date <= 21) or (mont == '07' and (23 <= date <= 31)):
            c = horoscope[4]
            strengths = ['Warmth', 'Humor', 'Pride', 'Joy', 'Creativity', 'Passion', 'Generosity']
            weakness = ['Arrogance', 'Stubbornness', 'Inflexibility', 'Laziness']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '09' and date <= 24) or (mont == '08' and (22 <= date <= 31)):
            c = horoscope[5]
            strengths = ['Practical', 'Loyal', 'Hardworking', 'Analytical', 'Kind']
            weakness = ['Worry', 'Shyness', 'All Work and No Play']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '10' and date <= 23) or (mont == '09' and (24 <= date <= 30)):
            c = horoscope[6]
            strengths = ['Social', 'Fair Minded', 'Cooperative', 'Diplomatic', 'Gracious']
            weakness = ['Indecisive', 'Carrying Grudge', 'Self Pity']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '11' and date <= 22) or (mont == '10' and (24 <= date <= 31)):
            c = horoscope[7]
            strengths = ['Passionate', 'Stubborn', 'Resourceful', 'Brave', 'A True Friend']
            weakness = ['Jealous', 'Distrusting', 'Secritive', 'Violent', 'Caustic']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '12' and date <= 22) or (mont == '11' and (23 <= date <= 30)):
            c = horoscope[8]
            strengths = ['Practical', 'Loyal', 'Hardworking', 'Analytical', 'Kind']
            weakness = ['Impatience', 'Silly Arguments', 'Fear To limit Choices']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '01' and date <= 20) or (mont == '12' and (23 <= date <= 31)):
            c = horoscope[9]
            strengths = ['Responsible', 'Good manners', 'Self Control', 'Disciplined']
            weakness = ['Unforgiving', 'expecting The Worst']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '02' and date <= 19) or (mont == '01' and (21 <= date <= 31)):
            c = horoscope[10]
            strengths = ['Progressive', 'Original',  'Independent', 'Humanitarian']
            weakness = ['Aloof', 'Secretive', 'Violent', 'Caustic']
            return render_template('result.html', title='Result', sign=c, dob=dob, stre=random.choice(strengths), weak=
                                   random.choice(weakness))
        if (mont == '03' and date <= 20) or (mont == '02' and (20 <= date <= 28)):
            c = horoscope[11]
            strengths = ['gentle', 'Wise', 'Musical']
            weakness = ['fearful', 'overly Trusting', 'Sad']
            return render_template('result.html', title='Result', sign=c, dob=dob)


if __name__ == '__main__':
    app.run(debug=True)