import { Page, Locator, expect } from '@playwright/test'
import { BasePage } from './BasePage'

export class LoginPage extends BasePage {
  readonly emailAddress: Locator
  readonly password: Locator
  readonly loginButton: Locator
  readonly accountHeader: Locator
  readonly accountEmailConfirm: Locator

  constructor(page: Page) {
    super(page)
    this.emailAddress = page.getByLabel('Email address')
    this.password = page.getByLabel('Password')
    this.loginButton = page.getByRole('button', { name: 'Login' })
    this.accountHeader = page.getByRole('heading', { name: 'Your Account' })
    this.accountEmailConfirm = page.getByText(
      /You are viewing the account for/i,
    )
  }

  async open() {
    await this.goto('/login')
  }

  async login(email: string, pass: string) {
    await this.emailAddress.fill(email)
    await this.password.fill(pass)
    await this.loginButton.click()
  }

  async expectLoggedInAs(email: string): Promise<void> {
    await expect(this.accountHeader).toBeVisible()
    await expect(this.accountEmailConfirm).toContainText(email)
  }
}
