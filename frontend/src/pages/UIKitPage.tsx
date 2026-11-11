import { Divider, Typography } from 'antd';
import ColorsSection from '../components/UIKitSections/ColorsSection';
import TypographySection from '../components/UIKitSections/TypographySection';
import ButtonsSection from '../components/UIKitSections/ButtonsSection';
import TablesSection from '../components/UIKitSections/TablesSection';

function UIKitPage() {
  return (
    <div className="mx-auto max-w-[1040px]">
      <header>
        <Typography.Title level={1} style={{ margin: '0 0 20px' }}>
          FINO UI Kit
        </Typography.Title>
        <Typography.Text style={{ margin: '0 0 20px' }}>
          Все элементы дизайн-системы
        </Typography.Text>
      </header>
      <Divider />
      <ColorsSection />
      <Divider />
      <TypographySection />
      <Divider />
      <ButtonsSection />
      <Divider />
      <TablesSection />
    </div>
  );
}

export default UIKitPage;
