import { Route, Routes } from 'react-router-dom';
import HomePage from '../pages/HomePage';
import Layout from '../layouts/Layout';
import UIKitLayout from '../layouts/UIKitLayout';
import UIKitPage from '../pages/UIKitPage';

function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="*" element={<h1>Страница не найдена.</h1>} />
        <Route path="/" element={<HomePage />} />
      </Route>
      <Route element={<UIKitLayout />}>
        <Route path="/ui-kit" element={<UIKitPage />} />
      </Route>
    </Routes>
  );
}

export default App;
