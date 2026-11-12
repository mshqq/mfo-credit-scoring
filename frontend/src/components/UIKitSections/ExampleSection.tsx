import { Tag, Card, Flex, Typography, Divider, Button } from 'antd';
import { useState } from 'react';
import { statuses } from './TablesSection.data';

export default function ExampleSection() {
  const [decision, setDecision] = useState<'pending' | 'approved' | 'rejected' | 'draft'>(
    'pending',
  );
  const status = statuses[decision];

  return (
    <section id="example">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Пример использования</Typography.Title>
        <Typography.Text type="secondary">
          Карточка заявки с данными клиента и кнопками решения.
        </Typography.Text>
      </Flex>
      <Card style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}>
        <Flex align="flex-start" justify="space-between">
          <Flex vertical gap={6}>
            <Typography.Text type="secondary" style={{ fontWeight: '600' }}>
              ЗАЯВКА №10482
            </Typography.Text>
            <Typography.Title level={3} style={{ margin: 0 }}>
              Иванов Иван Иванович
            </Typography.Title>
          </Flex>
          <Tag color={status.color}>{status.label}</Tag>
        </Flex>
        <Divider />
        <Flex gap={31}>
          <Flex vertical style={{ borderRight: '1px solid #bebebe', paddingRight: '31px' }}>
            <Typography.Text type="secondary">Сумма займа</Typography.Text>
            <Typography.Title level={3} style={{ margin: 0 }}>
              50 000 ₽
            </Typography.Title>
          </Flex>
          <Flex vertical>
            <Typography.Text type="secondary">Срок</Typography.Text>
            <Typography.Title level={3} style={{ margin: 0 }}>
              30 дней
            </Typography.Title>
          </Flex>
        </Flex>
        <Divider />
        <Flex gap={14}>
          <Button
            type="primary"
            onClick={() => setDecision('approved')}
            disabled={decision === 'approved'}
          >
            Одобрить
          </Button>
          <Button danger onClick={() => setDecision('rejected')} disabled={decision === 'rejected'}>
            Отклонить
          </Button>
        </Flex>
      </Card>
    </section>
  );
}
