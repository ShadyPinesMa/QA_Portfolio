import { Page, Locator } from '@playwright/test'
import { BasePage } from './BasePage'

export class ProductPage extends BasePage {
  readonly productHeader: Locator

  constructor(page: Page) {
    super(page)
    this.productHeader = page.getByRole('heading', { name: 'Browse sweets' })
  }

  async open() {
    await this.goto('/sweets')
  }

  protected addToBasketButtonFor(productName: string): Locator {
    return this.page.locator(`[data-name="${productName}"]`)
  }

  async addProductToBasket(productName: string) {
    await this.addToBasketButtonFor(productName).click()
  }
}
