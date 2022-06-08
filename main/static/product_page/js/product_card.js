const tabsText = document.querySelectorAll('.tabs__text');
    tabsText.forEach(el => el.addEventListener('click', setClassTab));

    function setClassTab(e){
        const productPerfomance = document.querySelectorAll('.product__perfomance');

        if(e.target.getAttribute('data-tabs') == 'feature'){
            productPerfomance[1].style.display = 'none';
            productPerfomance[0].style.display = 'block';
        }
        if(e.target.getAttribute('data-tabs') == 'instructions'){
            productPerfomance[0].style.display = 'none';
            productPerfomance[1].style.display = 'block';
        }

        tabsText.forEach(el => el.classList.remove('tab-choice'));
        e.target.classList.add('tab-choice');
    }

