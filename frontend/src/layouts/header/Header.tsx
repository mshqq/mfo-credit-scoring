import { Phone } from 'lucide-react';
import styles from './Header.module.css';
import logo from '../../assets/logo.png';

function Header() {
  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <div className={styles.logo}>
          <img src={logo} className={styles.logo_img}></img>
          <div className={styles.logo_p}>
            <p>FINO</p>
            <p>МИКРОФИНАНСОВАЯ ОРГАНИЗАЦИЯ</p>
          </div>
        </div>
        <nav>
          <a href="/">Преимущества</a>
          <a href="/">Как получить?</a>
          <a href="/">Условия</a>
          <a href="/">Документы</a>
        </nav>
        <a href="tel:+79141234567">
          <Phone />
          <span>+7 (914) 123-45-67</span>
        </a>
      </div>
    </header>
  );
}

export default Header;
