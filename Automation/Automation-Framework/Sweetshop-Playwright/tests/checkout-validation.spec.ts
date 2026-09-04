import { test, expect } from '@playwright/test'
import { BasketPage } from '../pages/BasketPage'

test('shows an error when first name is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ firstName: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Valid first name is required')).toBeVisible()
})

test('shows an error when last name is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ lastName: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Valid last name is required')).toBeVisible()
})

test('shows an error when email is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ email: '' })
  await basketPage.confirmOrderButton.click()

  await expect(
    page.getByText('Please enter a valid email address for shipping updates'),
  ).toBeVisible()
})

test('shows an error when postcode is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ postcode: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Postcode required')).toBeVisible()
})

test('shows an error when card name is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ cardName: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Name on card is required')).toBeVisible()
})

test('shows an error when card number is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ cardNumber: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Credit card number is required')).toBeVisible()
})

test('shows an error when expiration date is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ expDate: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Expiration date required')).toBeVisible()
})

test('shows an error message when cvv code is missing', async ({ page }) => {
  const basketPage = new BasketPage(page)
  await basketPage.open()

  await basketPage.fillCheckoutForm({ cvv: '' })
  await basketPage.confirmOrderButton.click()

  await expect(page.getByText('Security code required')).toBeVisible()
})
