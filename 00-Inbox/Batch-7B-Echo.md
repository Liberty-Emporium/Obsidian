# Echo Task Batch 7B — Email + SMS (Session 6)

## P0 — EMAIL SYSTEM (store app, branch: main)
PREREQ: Jay provides Gmail address + App Password. Set as Railway env vars: MAIL_SERVER=smtp.gmail.com, MAIL_PORT=587, MAIL_USE_TLS=true, MAIL_USERNAME=<gmail>, MAIL_PASSWORD=<app_password>

1. **Order Confirmation Email**:
   - After customer places order, send HTML email to their address
   - Template includes: order number, items (image thumbnails + names + prices + quantities), subtotal, discount applied, total, shipping address, tracking link
   - Use Flask-Mail or smtplib. Store email templates as Jinja2 templates in templates/emails/
   - Send asynchronously (use a thread or Celery) so checkout doesn't slow down

2. **Admin New Order Notification**:
   - When any order is placed, send email to leprograms@protonmail.com (or the admin Gmail)
   - Simple text email: "New order #1234 from John Doe — $89.99 — View: <admin link>"

3. **Newsletter System** at /admin/marketing:
   - List all collected subscriber emails with date added
   - Compose rich text email (use a WYSIWYG editor like TinyMCE or Quill — CDN)
   - Preview before sending
   - Send to all subscribers (batch send, 50 per second to avoid rate limits)
   - Track: sent count, timestamp, subject line
   - CSV export of subscriber list

4. **Shipping Notification Email**:
   - When admin marks order as "Shipped", auto-send email to customer
   - Include: tracking number (if provided), estimated delivery, link to /track-order

## P1 — SMS NOTIFICATIONS (store app, branch: main)
PREREQ: Jay provides Twilio credentials. Set as Railway env vars: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

5. **Twilio Integration**:
   - Install twilio Python package
   - Create /api/sms/send endpoint (admin auth required)
   - Test endpoint: send a test SMS to Jay's phone number

6. **Order SMS to Customer**:
   - At checkout, add optional "Phone number for SMS updates" field
   - When order is placed → SMS: "Thanks for your order #1234 from Liberty Emporium! Total: $89.99. Track: <link>"
   - When shipped → SMS: "Your order #1234 has shipped! Track: <link>"

7. **Admin SMS Alert**:
   - When new order over $100 is placed → SMS to Jay: "🎉 New order #1234 — $150.00 from John Doe"

## RULES
- Store → main branch
- DO NOT break the live store — Jay's mom is adding products
- Verify after every push
- POST completions to /api/tasks
- Write to 80-Daily/2026-05-28.md
- Don't touch Sweet Spot Cakes
