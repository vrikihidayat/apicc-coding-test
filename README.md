# apicc-coding-test

## User story

### Summary

Implement order status update via webhook and trigger customer notification

### Description

As a Business Operations Manager,
I want the system to automatically update order statuses via a webhook and notify the customer,
So that our internal records are always up-to-date and customers are kept informed about their order progress in real-time.

### Techincal Details
**Focus Area:** Security, Scalability, Integrity
- Create an endpoint that receives order status webhooks from a provider.
- When an order is updated to certain status, the system must "send" a message using a **MessageTemplate** model. Imagine that this function utilizes external messaging API (Whatsapp API or mailgun)