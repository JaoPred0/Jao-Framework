import { createElement } from './Utils.js'

function App() {
    const app = createElement('div', { class: 'app' },
        MainContent(),
    );

    document.getElementById('root').appendChild(app);
}

function MainContent() {
    return createElement('main', { class: 'app-main' },
        createElement('p', {}, 'Hello, World!')
    );
}


App();