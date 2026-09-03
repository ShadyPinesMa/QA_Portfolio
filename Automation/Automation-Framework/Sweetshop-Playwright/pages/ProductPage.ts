import { Page, Locator, expect } from '@playwright/test'
import { BasePage } from './BasePage'

export class ProductPage extends BasePage {
  readonly productHeader: Locator
  readonly basketLink: Locator

  constructor(page: Page) {
    super(page)
    this.productHeader = page.getByRole('heading', { name: 'Browse sweets' })
    this.basketLink = page.getByRole('link', { name: /basket/i })
  }

  async open() {
    await this.goto('/sweets')
  }
}
