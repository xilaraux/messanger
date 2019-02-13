(function() {
  const root = document.getElementById('root');

  import('./App.js').then((module) => {
    if (module && module.default) {
      const App = module.default;

      App.mount(root);
    }
  });
})();
