import ColorsSection from '../components/UIKitSections/ColorsSection';
import { TypographySection } from '../components/UIKitSections/TypographySection';

function UIKitPage() {
  return (
    <div>
      <header>
        <div>
          <h1>FINO UI Kit</h1>
          <p>Все элементы дизайн-системы</p>
        </div>
        <p>UI Kit</p>
      </header>
      <ColorsSection />
      <TypographySection />
    </div>
  );
}

export default UIKitPage;
