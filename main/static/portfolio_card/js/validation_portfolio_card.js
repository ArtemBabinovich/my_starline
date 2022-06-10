const cardFormBtn = document.querySelector('.card-form__btn');
    cardFormBtn.addEventListener('click', validationCard);

let cardText = document.querySelector('.card-form__input[type="text"]');
let cardTel = document.querySelector('.card-form__input[type="tel"]');
let errorText = document.querySelector('form.review-card__form .modal__error');

async function validationCard(e){
    e.preventDefault();
    const confirmModalTitle = document.querySelector('.m-confirm__title'),
        confirmModalText = document.querySelector('.m-confirm__subtitle');

    let re = /^((80|\+375)?)\s\((25|33|44|29)\)\s(\d{3})-(\d{2})-(\d{2})$/;

    let valid = re.test(cardTel.value);

    if(valid && cardText.value != ''){
        modal.classList.remove('m-show');
        confirmModalTitle.innerHTML = 'Мы получили вашу заявку';
        confirmModalText.innerHTML = 'Наш технический специалист перезвонит вам в течение 8 минут';
        confirmModal.classList.add('m-confirm-show');

        await fetch('', {
            method: 'POST',
            body: new FormData(document.querySelector('.review-card__form')),
        })
    } else{
        if(cardText.value != ''){
            cardText.classList.add('m-input-valid');
        } else{
            cardText.classList.add('m-input-error');
        }
        if(cardTel.value != '' && valid){
            cardTel.classList.add('m-input-valid');
            errorText.classList.remove('er-show');
        } else{
            cardTel.classList.add('m-input-error');
            errorText.classList.add('er-show');
        }
    }
}

confirmModal = document.querySelector('.m-confirm__wrapper');
    confirmModal.addEventListener('click', (event) => {
        if(event.target === document.querySelector('.m-confirm__cross')
            || event.target === document.querySelector('.m-confirm__wrapper')
            || event.target === document.querySelector('.m-confirm__btn')){
                confirmModal.classList.remove('m-confirm-show');
                document.body.classList.remove('body-h');
                cardText.classList.remove('m-input-valid');
                cardText.classList.remove('m-input-error');
                cardTel.classList.remove('m-input-valid');
                cardTel.classList.remove('m-input-error');
                errorText.classList.remove('er-show');
                cardTel.value = '';
                cardText.value = '';
        }
    });
