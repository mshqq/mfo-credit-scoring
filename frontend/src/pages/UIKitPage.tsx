import { Divider, Typography } from 'antd';
import ColorsSection from '../components/UIKitSections/ColorsSection';
import TypographySection from '../components/UIKitSections/TypographySection';
import ButtonsSection from '../components/UIKitSections/ButtonsSection';
import TablesSection from '../components/UIKitSections/TablesSection';
import TagsSection from '../components/UIKitSections/TagsSection';
import ExampleSection from '../components/UIKitSections/ExampleSection';
import InputsSection from '../components/UIKitSections/InputsSection';

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
      <InputsSection />
      <Divider />
      <TagsSection />
      <Divider />
      <TablesSection />
      <Divider />
      <ExampleSection />
    </div>
  );
}

export default UIKitPage;
