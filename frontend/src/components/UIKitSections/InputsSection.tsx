import { Card, Flex, Typography, Form, Input, Select, Checkbox, Button, Radio, Switch } from 'antd';

export default function InputsSection() {
  return (
    <section id="inputs">
      <Flex vertical align="baseline" style={{ marginBottom: '16px' }}>
        <Typography.Title level={2}>Элементы формы</Typography.Title>
        <Typography.Text type="secondary">
          Поля ввода, выбор значений, переключатели и состояния ошибок.
        </Typography.Text>
      </Flex>
      <div className="grid grid-cols-2 gap-6 items-start">
        <Card
          title="Данные клиента"
          style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}
        >
          <Form layout="vertical" requiredMark={false}>
            <Form.Item
              label="ФИО клиента"
              name="name"
              rules={[{ required: true, whitespace: true, message: 'Введите ФИО клиента' }]}
            >
              <Input placeholder="Иванов Иван Иванович" />
            </Form.Item>
            <Form.Item
              label="Сумма займа"
              name="amount"
              rules={[{ required: true, message: 'Выберите сумму займа' }]}
            >
              <Select
                placeholder="Выберите сумму"
                options={[
                  { value: 10000, label: '10 000 ₽' },
                  { value: 30000, label: '30 000 ₽' },
                  { value: 50000, label: '50 000 ₽' },
                ]}
              />
            </Form.Item>
            <Form.Item>
              <Checkbox>Согласен на обработку персональных данных</Checkbox>
            </Form.Item>
            <Button type="primary" htmlType="submit">
              Проверить данные
            </Button>
          </Form>
        </Card>
        <Card
          title="Состояния полей"
          style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}
        >
          <Flex vertical gap={4} style={{ marginBottom: '20px' }}>
            <label>Ошибка заполнения</label>
            <Input status="error" defaultValue="ivan@" />
            <Typography.Text type="danger">Введите email в формате name@example.ru</Typography.Text>
          </Flex>
          <Flex vertical gap={4}>
            <label>Недоступное поле</label>
            <Input value="Заявка № 10482" disabled />
            <Typography.Text type="secondary">Номер присваивается автоматически.</Typography.Text>
          </Flex>
        </Card>
        <Card
          title="Другие элементы"
          style={{ boxShadow: '0px 0px 50px 0px rgba(34, 60, 80, 0.15)' }}
          className="col-span-2"
        >
          <div className="grid grid-cols-2 gap-4">
            <Flex vertical gap={4}>
              <label className="mb-3">Пароль</label>
              <Input.Password placeholder="Введите пароль" />
              <Typography.Text type="secondary">
                Нажмите на значок глаза, чтобы показать пароль.
              </Typography.Text>
            </Flex>
            <Flex vertical gap={4} style={{ paddingBottom: '20px' }}>
              <label className="mb-3">Комментарий менеджера</label>
              <Input.TextArea
                placeholder="Например, удобное время для звонка"
                rows={3}
                maxLength={300}
                showCount
              />
            </Flex>
            <fieldset>
              <legend className="mb-3">Способ связи</legend>
              <Radio.Group
                defaultValue="phone"
                options={[
                  { value: 'phone', label: 'Телефон' },
                  { value: 'email', label: 'Email' },
                  { value: 'sms', label: 'СМС' },
                ]}
              />
            </fieldset>
            <Flex vertical gap={12}>
              <label>Уведомление о статусе заявки</label>
              <Flex gap={22}>
                <Switch defaultChecked checkedChildren="Вкл" unCheckedChildren="Выкл" />
                <Checkbox disabled>Недоступный вариант</Checkbox>
              </Flex>
            </Flex>
          </div>
        </Card>
      </div>
    </section>
  );
}
