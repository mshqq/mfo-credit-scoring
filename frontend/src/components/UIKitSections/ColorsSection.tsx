import { Button, Card, Flex, Tag, Typography } from 'antd';
import { ArrowRight } from 'lucide-react';
import { colorsItems, gradientColors, semanticColors, statusColors } from './ColorsSection.data';

export function ColorsSection() {
  return (
    <div>
      <div>
        <Typography.Title level={2}>Цвета</Typography.Title>
        <Typography.Text type="secondary">
          Цветовая палитра FINO на основе Ant Design
        </Typography.Text>
      </div>
      <Card style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}>
        <Typography.Title level={3}>Основная палитра</Typography.Title>
        <Flex justify="space-between">
          {colorsItems.map(({ label, color }) => (
            <div>
              <div
                style={{
                  backgroundColor: `${color}`,
                  width: 64,
                  height: 32,
                  borderRadius: 6,
                  boxShadow: '0px 0px 50px 0px rgba(0, 0, 0, 0.15)',
                }}
              ></div>
              <Typography.Text strong>{label}</Typography.Text>
              <p>{color}</p>
            </div>
          ))}
        </Flex>
      </Card>

      <Card>
        <Typography.Title level={3}>Семантические цвета</Typography.Title>
        <Flex justify="space-between">
          {semanticColors.map(({ label, color }) => (
            <div>
              <div
                style={{
                  backgroundColor: `${color}`,
                  width: 64,
                  height: 32,
                  borderRadius: 6,
                  boxShadow: '0px 0px 50px 0px rgba(0, 0, 0, 0.15)',
                }}
              ></div>
              <Typography.Text strong>{label}</Typography.Text>
              <p>{color}</p>
            </div>
          ))}
        </Flex>
      </Card>
      <Card>
        <Typography.Title level={3}>Градиенты</Typography.Title>
        <Flex vertical>
          {gradientColors.map(({ label, startColor, endColor }) => (
            <Flex>
              <div
                style={{
                  background: `linear-gradient(to right, ${startColor}, ${endColor})`,
                  width: 64,
                  height: 32,
                  borderRadius: 6,
                }}
              ></div>
              <Flex vertical>
                <Typography.Text>{label}</Typography.Text>
                <p>
                  {`${startColor}
                  ->s\
                  ${endColor}`}
                </p>
              </Flex>
            </Flex>
          ))}
        </Flex>
      </Card>
      <Card>
        <Typography.Title level={3}>Цвета статусов заявок</Typography.Title>
        <Flex gap={10}>
          {statusColors.map(({ label, color }) => (
            <Tag className="font-medium" color={color}>
              {label}
            </Tag>
          ))}
        </Flex>
      </Card>
      <Card>
        <Typography.Title level={3}>Примеры использования</Typography.Title>
        <Flex gap={8}>
          <Button
            style={{ background: 'linear-gradient(to right, #EC4899, #dd7cb1)' }}
            type="primary"
          >
            Оформить заявку
            <ArrowRight />
          </Button>
          <Button>Отмена</Button>
          <Button type="text" style={{ color: '#F9ABD4' }}>
            Подробнее
            <ArrowRight />
          </Button>
        </Flex>
      </Card>
    </div>
  );
}
