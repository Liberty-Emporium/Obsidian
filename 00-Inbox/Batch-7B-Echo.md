# Echo Task Batch 7B — Email + SMS

## PREREQ: Jay provides these credentials before starting:
- SendGrid API key (for email) → set as SENDGRID_API_KEY on Railway
- Twilio Account SID, Auth Token, Phone Number → set as TWILIO_SID, TWILIO_TOKEN, TWILIO_PHONE on Railway

## P0 — EMAIL (store app, branch: main)

1. **SendGrid Integration**: Install sendgrid Python package. Create /api/email/send endpoint (admin auth). Test with a test email.

2. **Order Confirmation Email**: After customer places order → send HTML email with items, total, order number, tracking link. Use Jinja2 template in templates/emails/order_confirmation.html.

3. **Admin New Order Notification**: New order → send email to admin address with order details and admin link.

4. **Shipping Notification**: When admin marks order "Shipped" → auto-send email to customer with tracking info.

5. **Newsletter System** at /admin/marketing: List subscribers, compose rich text email (use Quill CDN), preview, send to all. Track sent count + timestamp.

## P1 — SMS (store app, branch: main)

6. **Twilio Integration**: Install twilio Python package. Create /api/sms/send endpoint (admin auth). Send test SMS.

7. **Order SMS to Customer**: At checkout, optional "Phone for SMS updates" field. On order placed → SMS confirmation. On shipped → SMS with tracking.

8. **Admin SMS Alert**: New order over $100 → SMS to Jay's phone.

## RULES
- Store → main branch
- Verify after each push
- POST completions to /api/tasks
- Write to 80-Daily/2026-05-27.md
- Don't break existing features
