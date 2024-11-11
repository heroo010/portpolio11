from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
def Hero():
    popup('welcome app',
          put_text('اسم المدرسه؟').onclick(lambda: toast (".....اسم المدرسه:سعد بن معاز"))
    )

    put_html('<center><h3>استماره الطالب المقبول</h3></center>').style('background-color:black;color:#FF0303;font-weight:bold; padding:18px;')
    put_html('<center><p> تصدير السيره الزاتيه المؤهلين للدراسه</p></center>').style('font-weigth:bold;')
    put_html('<center><img src="https://i.top4top.io/p_3236md1n90.png" width="220",></center>')
    data=input_group(
        'يرجي ملئ جميع الحقول',
        [
            input('اسم الطالب' , name='stde'),
            input('عنوان الطالب' , name='loc'),
            input('البريد الالكتروني' , name='gmail'),
            input('رقم الهاتف' , name='phone'),
            radio('مؤهلات الطالب' , options=['ثانويه عامه','صنايع3','صنايع5'],name='certy'),
            checkbox('اتقان الغات' , options=['arabic' , 'english' , 'franse'] ,inline=True ,name='lang')
        ],
    )
    imgs=file_upload(
        'تحميل صوره شخصيه',
        accept='image/*',
        multiple=True
    )
    for img in imgs:
        global rr
        rr = img['content']

    put_text('stodent CV :*')
    put_table([
        ['الصوره الشخصيه','اسم الطالب','عنوان الطالب','الجيميل الخاص','رقم الموبايل','مؤهل الطالب','اللغه '],
        [put_image(rr).style('width:50px;'),data['stde'],data['loc'],data['gmail'],data['phone'],data['certy'],data['lang']]
    ])
start_server(Hero, port=4567 , debug=True)