import { Page, Locator } from '@playwright/test'
import { BasePage } from './BasePage'

export class HomePage extends BasePage {
  readonly homeHeader: Locator
  readonly browseSweetsButton: Locator

  constructor(page: Page) {
    super(page)
    this.homeHeader = page.getByRole('heading', {
      name: 'Welcome to the sweet shop!',
    })
    this.browseSweetsButton = page.getByRole('link', {
      name: 'Browse Sweets',
    })
  }

  async open() {
    await this.goto('/')
  }

  async goToProducts() {
    await this.browseSweetsButton.click()
  }
}
