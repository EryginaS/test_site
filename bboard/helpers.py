from docxtpl import DocxTemplate
from datetime import datetime


def doc_render_for_report(q):
    """
    q: Report object
    """
    TYPE_CHOICES_FOR_PRIORITY = {
        0:"Низкий", 
        1:"Средний", 
        2:"Высокий", 
    
    }
    TYPE_CHOICES_FOR_STATUS = {
        0:"Непрочитанный", 
        1:"К исполнению", 
        2:"Выполненный", 
    
    }
    TYPE_CHOICES_FOR_TYPE = {
        0:"Обслуживание", 
        1:"Консультация", 
    
    }
    file_ref = open("template.docx","rb")
    doc = DocxTemplate(file_ref)
    
    context = { 'director' : "И.И.Иванов", 'number':q.application.id, 'theme':q.theme, 'desc':q.desc,\
                'creator':q.report_maker}
    try:
        if q.client:
            context['client'] = q.client.first_name+" "+q.client.last_name
        else:
            context['client'] = 'Клиент не был найден.'
    except:
        pass
    try:
        if q.date:
            context['date'] = q.date
        else:
            context['date'] = 'Нет даты создания заявки.'
    except:
        pass
    try:
        if q.responsible:
            context['responsible']= q.responsible
        else:
            context['responsible']= 'Нет ответственного.'
    except:
        pass
    try:
        if q.priority or q.priority==0:
            context['priority']=TYPE_CHOICES_FOR_PRIORITY[q.priority]
        else:
            context['priority']='Поле не было заполнено.'     
    except:
        pass
    try:  
        if q.status or q.status==0:
            context['status']=TYPE_CHOICES_FOR_STATUS[q.status]
        else:
            context['status']='Поле не было заполнено.'
    except:
        pass
    try:
        if q.type_app or q.type_app==0:
            context['type_app']=TYPE_CHOICES_FOR_TYPE[q.type_app]
        else:
            context['type_app']='Поле не было заполнено.'
        
    except:
        pass
    try:
        if q.done_work:
            context['done_work']=q.done_work
        else:
            context['done_work']='Поле не было заполнено.'
    except:
        pass
    context['date_report_done'] = datetime.now()


    doc.render(context)
    return doc