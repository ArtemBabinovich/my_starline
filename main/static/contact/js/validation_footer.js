const formBtn = document.querySelector('.form__btn');
    formBtn.addEventListener('click', validationFormComment)


//! функция валидации футера, оставить отзыв
//* валидация с показанием окна, если все ок
async function validationFormComment(event){
    event.preventDefault();

    let re = /^((80|\+375)?)\s\((25|33|44|29)\)\s(\d{3})-(\d{2})-(\d{2})$/;
    let userPhone = document.querySelector('.footer__form [type="tel"]');
    let userName =  document.querySelector('.footer__form [type="text"]');
    let userTextArea = document.querySelector('.footer__form textarea');
    let errorText = document.querySelector('form.footer__form .modal__error');

    let valid = re.test(userPhone.value);

    if (valid && userName.value != '' && userPhone.value != '' && valid && userTextArea.value != ''){
        const confirmModal = document.querySelector('.m-confirm__wrapper');
            userName.classList.remove('m-input-error');
            userName.classList.remove('m-input-valid');
            userPhone.classList.remove('m-input-error');
            userPhone.classList.remove('m-input-valid');
            userTextArea.classList.remove('m-input-valid');
            userTextArea.classList.remove('m-input-error');
            errorText.classList.remove('er-show');
            userName.value = '';
            userPhone.value = '';
            userTextArea.value = '';
            confirmModal.classList.add('m-confirm-show');
            document.body.classList.add('body-h');

            await fetch('', {
                method: 'POST',
                body: new FormData(document.querySelector('.footer__form'))
            })
    } else{
        if(userName.value != ''){
            userName.classList.add('m-input-valid');
        } else{
            userName.classList.add('m-input-error');
        }
        if(userPhone.value != '' && valid){
            errorText.classList.remove('er-show');
            userPhone.classList.add('m-input-valid');
        } else{
            errorText.classList.add('er-show');
            userPhone.classList.add('m-input-error');
        }
        if(userTextArea.value != ''){
            userTextArea.classList.add('m-input-valid');
        } else{
            userTextArea.classList.add('m-input-error');
        }
    }
}
