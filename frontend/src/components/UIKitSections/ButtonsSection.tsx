import { App, Button, Card, Divider, Flex, Typography } from 'antd';
import { ArrowRight, ChevronRight, Search, UserPlus } from 'lucide-react';

export default function ButtonsSection() {
  const { message } = App.useApp();
  return (
    <section id="buttons">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Кнопки</Typography.Title>
        <Typography.Text type="secondary">Варианты, размеры и состояния кнопок.</Typography.Text>
      </Flex>
      <Card style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}>
        <Flex vertical style={{ padding: '8px 0' }}>
          <Typography.Text type="secondary" style={{ marginBottom: '12px' }}>
            Варианты
          </Typography.Text>
          <Flex gap={18}>
            <Button
              style={{ background: 'linear-gradient(to right, #EC4899, #dd7cb1)' }}
              type="primary"
              onClick={() => message.success('Заявка успешно оформлена!')}
            >
              Оформить заявку
              <ArrowRight />
            </Button>
            <Button onClick={() => message.info('Успешно отменено!')}>Отмена</Button>
            <Button type="text" style={{ color: '#F9ABD4' }}>
              Подробнее
              <ChevronRight />
            </Button>
            <Button onClick={() => message.success('Клиент успешно добавлен!')} type="dashed">
              <UserPlus />
              <span>Добавить клиента</span>
            </Button>
            <Button danger onClick={() => message.warning('Удалено!')}>
              Удалить
            </Button>
            <Button>
              <Search />
            </Button>
          </Flex>
        </Flex>
        <Divider />
        <Flex vertical style={{ padding: '8px 0' }}>
          <Typography.Text type="secondary" style={{ marginBottom: '12px' }}>
            Размеры
          </Typography.Text>
          <Flex gap={12} align="flex-end">
            <Button size="small" onClick={() => message.info('Маленькая кнопочка')}>
              Маленький
            </Button>
            <Button onClick={() => message.info('Средняя кнопочка')}>Средний</Button>
            <Button size="large" onClick={() => message.info('Большая кнопочка')}>
              Большой
            </Button>
          </Flex>
        </Flex>
        <Divider />
        <Flex vertical style={{ padding: '8px 0' }}>
          <Typography.Text type="secondary" style={{ marginBottom: '12px' }}>
            Состояния
          </Typography.Text>
          <Flex gap={14}>
            <Button type="primary" disabled>
              Недоступно
            </Button>
            <Button type="primary" loading>
              Обработка
            </Button>
          </Flex>
        </Flex>
      </Card>
    </section>
  );
}
