from flask import Blueprint, render_template, redirect, url_for, request
from helpers.database_handler import get_session_for_school, Matricula
from helpers.utils import check_token
from entry_data.entry_data import Register_Student

estudants_route = Blueprint('estudants', __name__)

@estudants_route.route('/<int:estudante_id>/update', methods=['GET', 'POST'])
def update_estudant(estudante_id):
    form = Register_Student()

    cookie_acess = request.cookies.get('acess_token')
    token_acess = check_token(cookie_acess)
    
    mapping_tokens = {
        'Colégio Dinâmico': 'colégiodinâmico',
        'School Test': 'testschool'
    }
    
    session = get_session_for_school(mapping_tokens.get(token_acess.get('sub')))
    
    estudant = session.query(Matricula).filter_by(id=estudante_id).first()
    
    if estudant:
        if request.method == 'POST':
            if form.validate_on_submit():
                estudant.aluno_name = form.aluno_name.data
                estudant.ano_letivo = form.ano_letivo.data
                estudant.status = form.status.data
                estudant.periodo_letivo = form.periodo_letivo.data
                estudant.modalidade = form.modalidade.data
                estudant.data_cancelamento = form.data_cancelamento.data
                estudant.notas_finais = form.notas_finais.data
                estudant.forma_pagamento = form.forma_pagamento.data
                estudant.observacoes = form.observacoes.data
                session.commit()
                return redirect(url_for('matriculas'))
            
    return render_template('create_matricula.html', form=form, estudant=estudant)

@estudants_route.route('/<int:estudante_id>/matrículas', methods=['GET', 'POST'])
def truncate(estudante_id):
    cookie_acess = request.cookies.get('acess_token')
    token_acess = check_token(cookie_acess)
    
    mapping_tokens = {
        'Colégio Dinâmico': 'colégiodinâmico',
        'School Test': 'testschool'
    }
    
    session = get_session_for_school(mapping_tokens.get(token_acess.get('sub')))
    
    estudant = session.query(Matricula).filter_by(id=estudante_id).first()
    print(estudant)
    
    if estudant:
        estudant.status = 'Trancada'
        session.commit()
        print(estudant.status)
        return redirect(url_for('matriculas'))
    
    
    return render_template('matriculas.html', estudante=estudant)
    