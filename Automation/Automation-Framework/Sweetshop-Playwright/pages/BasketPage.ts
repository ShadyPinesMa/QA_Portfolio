import { Page, Locator, expect } from '@playwright/test'
import { BasePage } from './BasePage'

type BillingInfo = {
  firstName?: string
  lastName?: string
  email?: string
  address?: string
  postcode?: string
}

type CardInfo = {
  cardName?: string
  cardNumber?: string
  expDate?: string
  cvv?: string
}

type CheckoutInfo = {
  firstName: string
  lastName: string
  email: string
  address: string
  postcode: string
  cardName: string
  cardNumber: string
  expDate: string
  cvv: string
}

const validCheckoutDefaults: CheckoutInfo = {
  firstName: 'Kira',
  lastName: 'Nerys',
  email: 'kira.nerys@ds9.org',
  address: '123 Promenade Way',
  postcode: 'BA1 2DS',
  cardName: 'Kira Nerys',
  cardNumber: '4567156865431234',
  expDate: '05/32',
  cvv: '189',
}

export class BasketPage extends BasePage {
  readonly firstName: Locator
  readonly lastName: Locator
  readonly email: Locator
  readonly address: Locator
  readonly postcode: Locator
  readonly cardName: Locator
  readonly cardNumber: Locator
  readonly expDate: Locator
  readonly cvv: Locator
  readonly confirmOrderButton: Locator

  constructor(page: Page) {
    super(page)
    this.firstName = page.locator('#name').first()
    this.lastName = page.locator('#name').nth(1)
    this.email = page.getByRole('textbox', { name: 'Email' })
    this.address = page.getByRole('textbox', { name: 'Address' })
    this.postcode = page.getByRole('textbox', { name: 'Postcode' })
    this.cardName = page.getByRole('textbox', { name: 'Name on card' })
    this.cardNumber = page.getByRole('textbox', { name: 'Credit card number' })
    this.expDate = page.getByRole('textbox', { name: 'Expiration CVV' })
    this.cvv = page.locator('#cc-cvv')
    this.confirmOrderButton = page.getByRole('button', {
      name: 'Confirm Order',
    })
  }

  async open() {
    await this.goto('/basket')
  }

  async fillBillingInfo(info: BillingInfo) {
    if (info.firstName !== undefined) await this.firstName.fill(info.firstName)
    if (info.lastName !== undefined) await this.lastName.fill(info.lastName)
    if (info.email !== undefined) await this.email.fill(info.email)
    if (info.address !== undefined) await this.address.fill(info.address)
    if (info.postcode !== undefined) await this.postcode.fill(info.postcode)
  }

  async fillCardInfo(info: CardInfo) {
    if (info.cardName !== undefined) await this.cardName.fill(info.cardName)
    if (info.cardNumber !== undefined)
      await this.cardNumber.fill(info.cardNumber)
    if (info.expDate !== undefined) await this.expDate.fill(info.expDate)
    if (info.cvv !== undefined) await this.cvv.fill(info.cvv)
  }

  async fillCheckoutForm(overrides: Partial<CheckoutInfo> = {}) {
    const info = { ...validCheckoutDefaults, ...overrides }
    await this.fillBillingInfo(info)
    await this.fillCardInfo(info)
  }
}
