import { type Page, Locator, expect } from '@playwright/test'

export class BasePage {
  readonly page: Page
  readonly sweetsLink: Locator
  readonly loginLink: Locator
  readonly basketLink: Locator

  constructor(page: Page) {
    this.page = page

    const nav = page.locator('nav')
    this.sweetsLink = nav.getByRole('link', { name: 'Sweets' })
    this.loginLink = nav.getByRole('link', { name: 'Login' })
    this.basketLink = nav.getByRole('link', { name: /basket/i })
  }

  async goto(path: string = '/') {
    await this.page.goto(path)
  }

  async title(): Promise<string> {
    return this.page.title()
  }

  async goToSweets() {
    await this.sweetsLink.click()
  }

  async goToLogin() {
    await this.loginLink.click()
  }

  async goToBasket() {
    await this.basketLink.click()
  }

  async getBasketCount(): Promise<number> {
    const text = await this.basketLink.textContent()
    const match = text?.match(/(\d+)\s*Basket/i)
    return match ? Number(match[1]) : 0
  }

  protected productHeading(productName: string): Locator {
    return this.page.getByRole('heading', { name: productName, exact: true })
  }

  protected addToBasketButtonFor(productName: string): Locator {
    return this.productHeading(productName).locator(
      'xpath=following::button[normalize-space()="Add to Basket"][1]',
    )
  }

  protected priceFor(productName: string): Locator {
    return this.productHeading(productName).locator(
      'xpath=following::*[starts-with(normalize-space(text()), "£")][1]',
    )
  }

  async getPriceText(productName: string): Promise<string | null> {
    return this.priceFor(productName).textContent()
  }

  async expectProductVisible(productName: string) {
    await expect(this.productHeading(productName)).toBeVisible()
  }
}
