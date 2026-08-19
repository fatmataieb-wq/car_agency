from odoo import models, fields

class CarRental(models.Model):
    _name = "car.rental"
    _description = "Car rental"
    _inherit = ["mail.thread"]  # pour avoir le suivi dans le chatter, comme dans ta démo
    name = fields.Char(
    string="Rental Reference",
    default="New",
    readonly=True,
    copy=False
)
    car_id = fields.Many2one("car.car", string="Car", required=True)
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")

    state = fields.Selection([
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("cancelled", "Cancelled"),
    ], string="Statut", default="draft", tracking=True)  # tracking=True = log dans le chatter

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancelled"})