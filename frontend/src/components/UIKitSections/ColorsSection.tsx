import { Card, Flex, Typography } from 'antd';
import { colorsItems, semanticColors } from './ColorsSection.data';

export default function ColorsSection() {
  return (
    <section id="colors">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Цвета</Typography.Title>
        <Typography.Text type="secondary">
          Цветовая палитра FINO на основе Ant Design.
        </Typography.Text>
      </Flex>
      <Card style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}>
        <Typography.Title level={3} style={{ fontSize: '20px' }}>
          Основная палитра
        </Typography.Title>
        <div className="grid grid-cols-6 gap-4">
          {colorsItems.map(({ label, color }) => (
            <Flex vertical key={label} gap={6}>
              <div
                style={{
                  backgroundColor: `${color}`,
                  width: 128,
                  height: 64,
                  borderRadius: 6,
                  boxShadow: '0px 0px 50px 0px rgba(0, 0, 0, 0.15)',
                }}
              ></div>
              <Flex vertical>
                <Typography.Text strong>{label}</Typography.Text>
                <Typography.Text type="secondary" style={{ fontSize: '12px' }}>
                  {color}
                </Typography.Text>
              </Flex>
            </Flex>
          ))}
        </div>
        <Typography.Title level={3} style={{ fontSize: '20px', margin: '28px 0 12px' }}>
          Семантические цвета
        </Typography.Title>
        <div className="grid grid-cols-4 gap-4">
          {semanticColors.map(({ label, color }) => (
            <Flex vertical key={label} gap={6}>
              <div
                style={{
                  backgroundColor: `${color}`,
                  width: 208,
                  height: 64,
                  borderRadius: 6,
                  boxShadow: '0px 0px 50px 0px rgba(0, 0, 0, 0.15)',
                }}
              ></div>
              <Flex vertical>
                <Typography.Text strong>{label}</Typography.Text>
                <Typography.Text type="secondary">{color}</Typography.Text>
              </Flex>
            </Flex>
          ))}
        </div>
        <Flex
          vertical
          style={{
            background: 'linear-gradient(to right, #EC4899, #BE185D)',
            padding: '24px',
            marginTop: '28px',
            borderRadius: 8,
            boxShadow: '0px 0px 50px 0px rgba(0, 0, 0, 0.15)',
          }}
        >
          <Typography.Text strong style={{ fontSize: '22px', color: '#FFFFFF' }}>
            Фирменный градиент
          </Typography.Text>
          <Typography.Text style={{ fontSize: '14px', color: '#FFFFFF' }}>
            Для акцентных блоков и обложек
          </Typography.Text>
        </Flex>
      </Card>
    </section>
  );
}
