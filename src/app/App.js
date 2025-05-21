function MainContent() {
    return (
        <main className="app-main">
            <p>Hello, World!</p>
        </main>
    );
}

function App() {
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<MainContent />);
}

App();