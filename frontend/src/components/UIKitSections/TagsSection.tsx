import { Card, Flex, Typography, Tag, Alert } from 'antd';

export default function TagsSection() {
  return (
    <section id="tags">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Статусы</Typography.Title>
        <Typography.Text type="secondary">Теги статусов и четыре вида уведомлений.</Typography.Text>
      </Flex>
      <Card style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}>
        <Flex gap={14} style={{ marginBottom: '22px' }}>
          <Tag color="#72C55F">Одобрено</Tag>
          <Tag color="#EF4444">Отказано</Tag>
          <Tag color="#f5a216">На проверке</Tag>
          <Tag>Черновик</Tag>
        </Flex>
        <div className="grid grid-cols-2 gap-6">
          <Alert
            showIcon
            title="Заявка на рассмотрении"
            description="Менеджер свяжется с клиентом после проверки."
          />
          <Alert
            showIcon
            title="Данные сохранены"
            description="Можно перейти к следующему шагу."
            type="success"
          />
          <Alert
            showIcon
            title="Проверьте документы"
            description="Для принятия решения нужны дополнительные сведения."
            type="warning"
          />
          <Alert
            showIcon
            title="Не удалось отправить заявку"
            description="Проверьте соединение и попробуйте ещё раз."
            type="error"
          />
        </div>
      </Card>
    </section>
  );
}
