import { Card, Divider, Flex, Typography } from 'antd';

export default function TypographySection() {
  return (
    <section id="typography">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Типографика</Typography.Title>
        <Typography.Text type="secondary">Заголовки, основной текст и подписи.</Typography.Text>
      </Flex>
      <Card style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}>
        <Flex vertical style={{ padding: '10px 0' }}>
          <Typography.Text type="secondary">Заголовок страницы ♡ 38 px</Typography.Text>
          <Typography.Title level={1} style={{ fontSize: '38px', margin: 0 }}>
            Заявки клиентов
          </Typography.Title>
        </Flex>
        <Divider />
        <Flex vertical style={{ padding: '10px 0' }}>
          <Typography.Text type="secondary">Заголовок секции ♡ 24 px</Typography.Text>
          <Typography.Title level={3} style={{ fontSize: '24px', margin: 0 }}>
            Заявка на заём
          </Typography.Title>
        </Flex>
        <Divider />
        <Flex vertical style={{ padding: '10px 0' }}>
          <Typography.Text type="secondary">Основной текст ♡ 14 px</Typography.Text>
          <Typography.Paragraph style={{ fontSize: '14px', margin: 0 }}>
            Заполните данные клиента, чтобы перейти к рассмотрению заявки.
          </Typography.Paragraph>
        </Flex>
        <Divider />
        <Flex vertical style={{ padding: '10px 0' }}>
          <Typography.Text type="secondary">Подпись ♡ 12 px</Typography.Text>
          <Typography.Text type="secondary" style={{ fontSize: '12px' }}>
            Все поля обязательны для заполнения
          </Typography.Text>
        </Flex>
      </Card>
    </section>
  );
}
