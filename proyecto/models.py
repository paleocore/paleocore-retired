# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# #
# # Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# # into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models
#
#
# class LaLagoFocalData(models.Model):
#     focal_data_id = models.IntegerField(db_column='Focal Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_long_time = models.CharField(db_column='Time Long_Time', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     number_5_min_sample_pt = models.CharField(db_column='5-min sample pt', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
#     time_focal_data_pt = models.CharField(db_column='Time focal data pt', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     behavior = models.CharField(db_column='Behavior', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     additional_info = models.CharField(db_column='Additional Info', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     partner = models.CharField(db_column='Partner', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     focal_carry_infant = models.CharField(db_column='Focal Carry Infant', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ptn_carry_infant = models.CharField(db_column='PTN Carry Infant', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juv_id = models.CharField(db_column='JUV ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juv_behavior = models.CharField(db_column='JUV Behavior', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juv_distance = models.CharField(db_column='JUV Distance', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_id = models.CharField(db_column='NN ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_behavior = models.CharField(db_column='NN Behavior', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_distance = models.CharField(db_column='NN Distance', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_carry_infant = models.CharField(db_column='NN Carry Infant', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_partner = models.CharField(db_column='NN Partner', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     con = models.CharField(db_column='CON', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     field_1 = models.CharField(db_column='<1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     field_2 = models.CharField(db_column='<2', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     field_5 = models.CharField(db_column='<5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     field_10 = models.CharField(db_column='<10', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     vocalizations_heard = models.CharField(db_column='Vocalizations heard', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'LA Lago Focal Data'
#
#
# class LaLagoFocalSamples(models.Model):
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', primary_key=True, max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     time_focal_start = models.CharField(db_column='Time Focal Start', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_focal_end = models.CharField(db_column='Time Focal End', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_duration = models.CharField(db_column='Focal Duration', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_animal = models.CharField(db_column='Focal Animal', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_age_sex_class = models.CharField(db_column='Focal Age/Sex Class', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     focal_completion = models.CharField(db_column='Focal Completion', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     transcription_date = models.CharField(db_column='Transcription Date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group = models.CharField(db_column='Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'LA Lago Focal Samples'
#
#
# class LaRangingData(models.Model):
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_data_id = models.IntegerField(db_column='Ranging Data ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
#     loc_m = models.CharField(db_column='Loc M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_deg = models.CharField(db_column='Loc Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_pto_ref = models.CharField(db_column='Loc Pto Ref', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     old_loc_pto_ref = models.CharField(db_column='Old Loc Pto Ref', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_comments = models.CharField(db_column='Ranging Comments', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_activity = models.CharField(db_column='Group Activity', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_notes = models.TextField(db_column='Ranging Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     immediate_spread = models.CharField(db_column='Immediate Spread', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     immediate_sgc = models.CharField(db_column='Immediate SGC', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     overall_spread = models.CharField(db_column='Overall Spread', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     overall_sgc = models.CharField(db_column='Overall SGC', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     associated_with = models.CharField(db_column='Associated With', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     association_distance = models.CharField(db_column='Association Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_avg_error = models.CharField(db_column='GPS Avg Error', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_dop = models.CharField(db_column='GPS DOP', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_navigation = models.CharField(db_column='GPS Navigation', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     over_flood = models.NullBooleanField(db_column='Over Flood')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     on_the_fly_location = models.CharField(db_column='On The Fly Location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'LA Ranging Data'
#
#
# class OldLocations(models.Model):
#     location_id = models.FloatField(db_column='Location ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     x_coord = models.FloatField(db_column='X Coord', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     y_coord = models.FloatField(db_column='Y Coord', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     trail_or_tree = models.CharField(db_column='Trail or Tree', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     aka_1 = models.CharField(db_column='AKA 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     aka_2 = models.CharField(db_column='AKA 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'OLD locations'
#
#
# class AcousticContactDistance(models.Model):
#     acoustic_contact_distance_id = models.IntegerField(db_column='Acoustic Contact Distance ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     acoustic_contact_distance = models.CharField(db_column='Acoustic Contact Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'acoustic contact distance'
#
#
# class AdLibData(models.Model):
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ad_lib_data_id = models.IntegerField(db_column='Ad Lib Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_start = models.DateTimeField(db_column='Time Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_end = models.DateTimeField(db_column='Time End', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     actor = models.CharField(db_column='Actor', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     behavior = models.CharField(db_column='Behavior', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     recipient_partner = models.CharField(db_column='Recipient-Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     description_notes = models.TextField(db_column='Description-Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     key_words = models.CharField(db_column='Key Words', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     begin_late = models.NullBooleanField(db_column='Begin Late')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_early = models.NullBooleanField(db_column='End Early')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_m = models.CharField(db_column='Loc M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     log_deg = models.CharField(db_column='Log Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     reference_point = models.CharField(db_column='Reference Point', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     context = models.CharField(db_column='Context', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     is_outside_subgroup = models.NullBooleanField(db_column='Is Outside Subgroup')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     is_initiation = models.NullBooleanField(db_column='Is Initiation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     is_response = models.NullBooleanField(db_column='Is Response')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gets_response = models.NullBooleanField(db_column='Gets Response')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'ad lib data'
#
#
# class AgeSexClasses(models.Model):
#     age_sex_class_id = models.IntegerField(db_column='Age-Sex Class ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     age_sex_class_sort_id = models.IntegerField(db_column='Age-Sex Class Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     age_sex_class = models.CharField(db_column='Age-Sex Class', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'age-sex classes'
#
#
# class AnimalIds(models.Model):
#     animal_id = models.IntegerField(db_column='Animal ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     animal_name = models.CharField(db_column='Animal Name', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     short_name = models.CharField(db_column='Short Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group = models.CharField(db_column='Group', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     taxon = models.CharField(db_column='Taxon', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     age_sex = models.CharField(db_column='Age/Sex', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_of_birth = models.DateTimeField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_of_birth_est = models.NullBooleanField(db_column='Date of Birth Est')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_of_loss = models.DateTimeField(db_column='Date of Loss', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     image_path = models.CharField(db_column='Image Path', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#     collar_type = models.CharField(db_column='Collar Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     collar_details = models.TextField(db_column='Collar Details', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_first_captured = models.DateTimeField(db_column='Date First Captured', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     current_group_member = models.NullBooleanField(db_column='Current Group Member')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_added_to_dbase = models.DateTimeField(db_column='Date Added to DBASE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'animal ids'
#
#
# class AnimalIdsMonogamous(models.Model):
#     id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     taxon = models.CharField(db_column='Taxon', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     group = models.CharField(db_column='Group', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     individual = models.CharField(db_column='Individual', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     id_code = models.CharField(db_column='ID code', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sex = models.CharField(db_column='Sex', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     dat_first_observed = models.DateTimeField(db_column='Dat first observed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     age_class_first_observed = models.CharField(db_column='Age class first observed', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_mother_last_obs_w_o_inf = models.DateTimeField(db_column='Date mother last obs w/o INF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_mother_first_obs_w_inf = models.DateTimeField(db_column='Date mother first obs w/ INF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     current_group_member = models.NullBooleanField(db_column='Current group member')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     last_day_observed = models.DateTimeField(db_column='Last day observed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     first_day_missing = models.DateTimeField(db_column='First day missing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fate = models.CharField(db_column='Fate', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     recognition_characteristics = models.TextField(db_column='Recognition characteristics', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     collar_type = models.CharField(db_column='Collar type', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_collared = models.DateTimeField(db_column='Date collared', unique=True, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     details_collar = models.TextField(db_column='Details collar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'animal ids monogamous'
#
#
# class AtelesVocalData(models.Model):
#     vocalization_id = models.IntegerField(db_column='Vocalization ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.ForeignKey('FocalSamples', db_column='Focal Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time = models.CharField(db_column='Time', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     vocalization_type = models.CharField(db_column='Vocalization Type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     vocalizer_id = models.CharField(db_column='Vocalizer ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_within_subgroup = models.NullBooleanField(db_column='Voc within Subgroup')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     angle_to_voc = models.CharField(db_column='Angle to Voc', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     est_distance_to_voc = models.CharField(db_column='Est Distance to Voc', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     context = models.CharField(db_column='Context', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
#     time_end = models.CharField(db_column='Time End', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'ateles vocal data'
#
#
# class Avistajes(models.Model):
#     obs_sample_id = models.ForeignKey('ObserverSamples', db_column='Obs Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     avistaje_id = models.CharField(db_column='Avistaje ID', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     taxon = models.CharField(db_column='Taxon', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     group = models.CharField(db_column='Group', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     time_enc = models.DateTimeField(db_column='Time Enc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_enc_m = models.CharField(db_column='Loc Enc M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_enc_deg = models.CharField(db_column='Loc Enc Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_enc_pto_ref = models.CharField(db_column='Loc Enc Pto Ref', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     enc_loc_comments = models.CharField(db_column='Enc Loc Comments', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     beh_when_enc = models.CharField(db_column='Beh When Enc', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_left_lost = models.DateTimeField(db_column='Time Left/Lost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_left_lost_m = models.CharField(db_column='Loc Left/Lost M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_left_lost_deg = models.CharField(db_column='Loc Left/Lost Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_end_pto_ref = models.CharField(db_column='Loc End Pto Ref', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_loc_comments = models.CharField(db_column='End Loc Comments', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     how_ended = models.CharField(db_column='How Ended', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     avistaje_notes = models.TextField(db_column='Avistaje Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     data_book = models.CharField(db_column='Data Book', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     av_rev_by_pi = models.NullBooleanField(db_column='AV Rev by PI')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     av_rev_by_assistant = models.NullBooleanField(db_column='AV Rev By Assistant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     vocalizations_heard = models.NullBooleanField(db_column='Vocalizations Heard')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_distance = models.CharField(db_column='Voc Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_avg_err_enc = models.IntegerField(db_column='GPS Avg Err Enc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_navigation_enc = models.CharField(db_column='GPS Navigation Enc', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_avg_err_end = models.IntegerField(db_column='GPS Avg Err End', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_navigation_end = models.CharField(db_column='GPS Navigation End', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_observer_present = models.CharField(db_column='Other Observer Present', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     response_to_playback = models.NullBooleanField(db_column='Response to Playback')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     follow_data_included = models.NullBooleanField(db_column='Follow Data Included')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     on_the_fly_enc_location = models.CharField(db_column='On The Fly Enc Location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     on_the_fly_end_location = models.CharField(db_column='On The Fly End Location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     duets = models.NullBooleanField(db_column='Duets')  # Field name made lowercase.
#     aggression = models.NullBooleanField(db_column='Aggression')  # Field name made lowercase.
#     army_ant_eating = models.NullBooleanField(db_column='Army Ant Eating')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     intergroup_encounter = models.NullBooleanField(db_column='Intergroup Encounter')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     grooming = models.NullBooleanField(db_column='Grooming')  # Field name made lowercase.
#     sexual_behavior = models.NullBooleanField(db_column='Sexual Behavior')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     scent_marking = models.NullBooleanField(db_column='Scent Marking')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_complete = models.NullBooleanField(db_column='Group Complete')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     no_summary_comments_apply = models.NullBooleanField(db_column='No Summary Comments Apply')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     monogamy_project = models.NullBooleanField(db_column='Monogamy Project')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     atelines_project = models.NullBooleanField(db_column='Atelines Project')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'avistajes'
#
#
# class BiologicalSampleTypes(models.Model):
#     biological_sample_type_id = models.IntegerField(db_column='Biological Sample Type ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'biological sample types'
#
#
# class BiologicalSamples(models.Model):
#     obs_sample_id = models.CharField(db_column='Obs Sample ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     biological_sample_label = models.CharField(db_column='Biological Sample Label', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_date = models.DateTimeField(db_column='Sample Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_time = models.DateTimeField(db_column='Sample Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     type_of_sample = models.CharField(db_column='Type of Sample', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     related_avistaje_id = models.CharField(db_column='Related Avistaje ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     taxon = models.CharField(db_column='Taxon', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     group = models.CharField(db_column='Group', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     site = models.CharField(db_column='Site', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     collected_by = models.CharField(db_column='Collected By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_status = models.CharField(db_column='Sample Status', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     export_carrier_of_samples = models.CharField(db_column='Export Carrier of Samples', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     original_proyecto_primates_sample_number = models.CharField(db_column='Original Proyecto Primates Sample Number', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     alternate_sample_name = models.CharField(db_column='Alternate Sample Name', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_loc_m = models.CharField(db_column='Sample Loc M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_loc_deg = models.CharField(db_column='Sample Loc Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_loc_pto_ref = models.CharField(db_column='Sample Loc Pto Ref', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     storage_medium = models.CharField(db_column='Storage Medium', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     container = models.CharField(db_column='Container', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     individual = models.CharField(db_column='Individual', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     sex_class = models.CharField(db_column='Sex Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     age_class = models.CharField(db_column='Age Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
#     former_sample_id = models.CharField(db_column='Former Sample ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     hormone_extraction_by = models.CharField(db_column='Hormone Extraction By', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_extracted = models.DateTimeField(db_column='Time Extracted', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_on_ice = models.NullBooleanField(db_column='Sample on Ice')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     amount_extracted_mg_field = models.CharField(db_column='Amount Extracted (mg)', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     number_of_seeds_in_sample = models.CharField(db_column='Number of Seeds in Sample', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     number_of_species_in_sample = models.CharField(db_column='Number of Species in Sample', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     names_of_species_in_sample = models.CharField(db_column='Names of Species in Sample', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     auto_number_sample_id = models.IntegerField(db_column='Auto Number Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_gps_dop = models.CharField(db_column='Sample GPS DOP', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_gps_navigation = models.CharField(db_column='Sample GPS Navigation', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sample_gps_avg_error = models.CharField(db_column='Sample GPS Avg Error', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     on_the_fly_location = models.CharField(db_column='On The Fly Location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     hormone_tube_name = models.CharField(db_column='Hormone Tube Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     parasites = models.NullBooleanField(db_column='Parasites')  # Field name made lowercase.
#     estimated_sample_volume = models.CharField(db_column='Estimated Sample Volume', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'biological samples'
#
#
# class CameraTrapRevision(models.Model):
#     obs_sample_id = models.ForeignKey('ObserverSamples', db_column='Obs Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     camera_trap_revision_id = models.IntegerField(db_column='Camera Trap Revision ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     revision_number = models.CharField(db_column='Revision Number', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     revision_date = models.DateTimeField(db_column='Revision Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     revision_time = models.DateTimeField(db_column='Revision Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     observer = models.CharField(db_column='Observer', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     deploy_test_okay = models.NullBooleanField(db_column='Deploy Test Okay')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     arrival_test_okay = models.NullBooleanField(db_column='Arrival Test Okay')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     number_of_images = models.CharField(db_column='Number of Images', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     is_memory_full = models.NullBooleanField(db_column='Is Memory Full')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_of_last_image = models.DateTimeField(db_column='Date of Last Image', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_of_last_image = models.DateTimeField(db_column='Time of Last Image', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     battery_level = models.CharField(db_column='Battery Level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     batteries_changed = models.NullBooleanField(db_column='Batteries Changed')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     memory_card_changed = models.NullBooleanField(db_column='Memory Card Changed')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     memory_card_size = models.CharField(db_column='Memory Card Size', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     image_quality = models.CharField(db_column='Image Quality', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     problems_notes = models.TextField(db_column='Problems/Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_test_done = models.NullBooleanField(db_column='End Test Done')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     begin_test_done = models.NullBooleanField(db_column='Begin Test Done')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mineral_lick_name = models.CharField(db_column='Mineral Lick Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     camera_trap_name = models.CharField(db_column='Camera Trap Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     photo_delay = models.CharField(db_column='Photo Delay', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     capture_mode = models.CharField(db_column='Capture Mode', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     multishot_count = models.CharField(db_column='Multishot Count', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     video_length = models.CharField(db_column='Video Length', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     new_memory_card_size = models.CharField(db_column='New Memory Card Size', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     new_capture_mode = models.CharField(db_column='New Capture Mode', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     new_image_quality = models.CharField(db_column='New Image Quality', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     new_photo_delay = models.CharField(db_column='New Photo Delay', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     new_multishot_count = models.CharField(db_column='New Multishot Count', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_deployed = models.DateTimeField(db_column='Time Deployed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     new_video_length = models.CharField(db_column='New Video Length', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sensitivity = models.CharField(db_column='Sensitivity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     new_sensitivity = models.CharField(db_column='New Sensitivity', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'camera trap revision'
#
#
# class CaptureRecord(models.Model):
#     capture_id = models.IntegerField(db_column='Capture ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     obs_sample_id = models.ForeignKey('ObserverSamples', db_column='Obs Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     capture_date = models.DateTimeField(db_column='Capture Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     darter = models.CharField(db_column='Darter', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     species = models.CharField(db_column='Species', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sex = models.CharField(db_column='Sex', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     age_class_when_captured = models.CharField(db_column='Age Class when Captured', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     subject = models.CharField(db_column='Subject', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     method = models.CharField(db_column='Method', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     initial_dosage = models.CharField(db_column='Initial Dosage', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     where_hit = models.CharField(db_column='Where Hit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_hit = models.CharField(db_column='Time Hit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_fell = models.CharField(db_column='Time Fell', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     how_recovered = models.CharField(db_column='How Recovered', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     habitat = models.CharField(db_column='Habitat', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     darted_ref_pt = models.CharField(db_column='Darted Ref Pt', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     darted_m = models.CharField(db_column='Darted M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     darted_deg = models.CharField(db_column='Darted Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     second_dosage = models.CharField(db_column='Second Dosage', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     third_dosage = models.CharField(db_column='Third Dosage', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     second_dosage_time = models.DateTimeField(db_column='Second Dosage Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     third_dosage_time = models.DateTimeField(db_column='Third Dosage Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_released = models.CharField(db_column='Time Released', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     release_ref_pt = models.CharField(db_column='Release Ref Pt', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     release_m = models.CharField(db_column='Release M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     release_deg = models.CharField(db_column='Release Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     radiocollar_manufacturer = models.CharField(db_column='Radiocollar Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     serial_number = models.CharField(db_column='Serial Number', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     radiocollar_frequency = models.CharField(db_column='Radiocollar Frequency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     receiver_band_and_channel = models.CharField(db_column='Receiver Band and Channel', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_collar_activated = models.DateTimeField(db_column='Date Collar Activated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_collar_activated = models.CharField(db_column='Time Collar Activated', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     exam_by = models.CharField(db_column='Exam By', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     asymmetry = models.CharField(db_column='Asymmetry', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     broken_bones = models.CharField(db_column='Broken Bones', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     lacerations = models.CharField(db_column='Lacerations', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     missing_digits_or_nails = models.CharField(db_column='Missing Digits or Nails', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ectoparasites = models.CharField(db_column='Ectoparasites', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     abdominal_exam = models.CharField(db_column='Abdominal Exam', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     crt = models.CharField(db_column='CRT', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hydration = models.CharField(db_column='Hydration', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     breathing_1 = models.CharField(db_column='Breathing 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     breathing_2 = models.CharField(db_column='Breathing 2', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     breathing_3 = models.CharField(db_column='Breathing 3', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     heartbeat_1 = models.CharField(db_column='Heartbeat 1', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     heartbeat_2 = models.CharField(db_column='Heartbeat 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     heartbeat_3 = models.CharField(db_column='Heartbeat 3', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rectal_temp_1 = models.CharField(db_column='Rectal Temp 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rectal_temp_2 = models.CharField(db_column='Rectal Temp 2', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     rectal_temp_3 = models.CharField(db_column='Rectal Temp 3', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     check_time_1 = models.DateTimeField(db_column='Check Time 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     check_time_2 = models.DateTimeField(db_column='Check Time 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     check_time_3 = models.DateTimeField(db_column='Check Time 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     weight_grams_obs_1_no_bag = models.CharField(db_column='Weight (grams) Obs 1 No Bag', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     weight_grams_obs_2_no_bag = models.CharField(db_column='Weight (grams) Obs 2 No Bag', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     scale_used = models.CharField(db_column='Scale Used', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     head_and_body_length_cm_field = models.CharField(db_column='Head and Body Length (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     chest_girth_cm_field = models.CharField(db_column='Chest Girth (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     tail_length_from_dorsal_base_cm_field = models.CharField(db_column='Tail Length (from dorsal base) (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     tail_length_from_ventral_base_cm_field = models.CharField(db_column='Tail Length (from ventral base) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_leg_length_cm_field = models.CharField(db_column='Left Leg Length (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_foot_length_cm_field = models.CharField(db_column='Left Foot Length (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_arm_length_cm_field = models.CharField(db_column='Left Arm Length (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_hand_length_cm_field = models.CharField(db_column='Left Hand Length (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     neck_circumference_cm_field = models.CharField(db_column='Neck Circumference (cm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_testis_length_mm_field = models.CharField(db_column='Left Testis Length (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_testis_breadth_mm_field = models.CharField(db_column='Left Testis Breadth (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     right_testis_length_mm_field = models.CharField(db_column='Right Testis Length (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     right_testis_breadth_mm_field = models.CharField(db_column='Right Testis Breadth (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     nipple_color = models.CharField(db_column='Nipple Color', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nipple_elongation = models.CharField(db_column='Nipple Elongation', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     scars_and_marks = models.CharField(db_column='Scars and Marks', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     photos_taken = models.CharField(db_column='Photos Taken', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     upper_right_canine_buccolingual_mm_field = models.CharField(db_column='Upper Right Canine Buccolingual (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     upper_right_canine_length_mm_field = models.CharField(db_column='Upper Right Canine Length (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     upper_left_canine_buccolingual_mm_field = models.CharField(db_column='Upper Left Canine  Buccolingual (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     upper_left_canine_length_mm_field = models.CharField(db_column='Upper Left Canine Length (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     lower_right_canine_buccolingual_mm_field = models.CharField(db_column='Lower Right Canine Buccolingual (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     lower_right_canine_length_mm_field = models.CharField(db_column='Lower Right Canine Length (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     lower_left_canine_buccolingual_mm_field = models.CharField(db_column='Lower Left Canine Buccolingual (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     lower_left_canine_length_mm_field = models.CharField(db_column='Lower Left Canine Length (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     canine_injuries = models.CharField(db_column='Canine Injuries', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     upper_incisor_wear = models.CharField(db_column='Upper Incisor Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     lower_incisor_wear = models.CharField(db_column='Lower Incisor Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     upper_canine_wear = models.CharField(db_column='Upper Canine Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     lower_canine_wear = models.CharField(db_column='Lower Canine Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     upper_premolar_wear = models.CharField(db_column='Upper Premolar Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     lower_premolar_wear = models.CharField(db_column='Lower Premolar Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     upper_molar_wear = models.CharField(db_column='Upper Molar Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     lower_molar_wear = models.CharField(db_column='Lower Molar Wear', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     general_health_and_nutritional_status = models.CharField(db_column='General Health and Nutritional Status', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     left_upper_arm_humerus_cm_field = models.CharField(db_column='Left Upper Arm (humerus) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_lower_arm_ulna_cm_field = models.CharField(db_column='Left Lower Arm (ulna) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_upper_leg_femur_cm_field = models.CharField(db_column='Left Upper Leg (femur) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_lower_leg_tibia_cm_field = models.CharField(db_column='Left Lower Leg (tibia) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     max_length_of_head_mm_field = models.CharField(db_column='Max Length of Head (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     max_cranial_breadth_mm_field = models.CharField(db_column='Max Cranial Breadth (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     postorbital_breadth_mm_field = models.CharField(db_column='Postorbital Breadth (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     muzzle_length_mm_field = models.CharField(db_column='Muzzle Length (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     max_left_ear_length_mm_field = models.CharField(db_column='Max Left Ear Length (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     max_left_ear_breadth_mm_field = models.CharField(db_column='Max Left Ear Breadth (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     biorbital_breadth_mm_field = models.CharField(db_column='Biorbital Breadth (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     least_interorbital_breadth_mm_field = models.CharField(db_column='Least Interorbital Breadth (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_nostril_breadth_mm_field = models.CharField(db_column='Left Nostril Breadth (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_nostril_height_mm_field = models.CharField(db_column='Left Nostril Height (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_thumb_length_wrist_to_tip_of_1st_digit_cm_field = models.CharField(db_column='Left Thumb Length (wrist to tip of 1st digit) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_big_toe_length_heel_to_tip_of_1st_digit_cm_field = models.CharField(db_column='Left Big Toe Length  (heel to tip of 1st digit) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_hand_span_1st_to_longest_digit_when_extended_cm_field = models.CharField(db_column='Left Hand Span (1st to longest digit when extended) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     left_foot_span_1st_to_longest_digit_when_extended_cm_field = models.CharField(db_column='Left Foot Span (1st to longest digit when extended) (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     hair_samples = models.NullBooleanField(db_column='Hair Samples')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     blood_samples = models.NullBooleanField(db_column='Blood Samples')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     tissue_samples = models.NullBooleanField(db_column='Tissue Samples')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     buccal_swabs = models.NullBooleanField(db_column='Buccal Swabs')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fibroblast_biopsy_samples = models.NullBooleanField(db_column='Fibroblast Biopsy Samples')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     feces = models.NullBooleanField(db_column='Feces')  # Field name made lowercase.
#     urine = models.NullBooleanField(db_column='Urine')  # Field name made lowercase.
#     dental_cast = models.NullBooleanField(db_column='Dental Cast')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
#     reviewed = models.NullBooleanField(db_column='Reviewed')  # Field name made lowercase.
#     released_with_group = models.NullBooleanField(db_column='Released with Group')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     digit_2_left_mm_field = models.CharField(db_column='Digit 2 Left (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     digit_4_left_mm_field = models.CharField(db_column='Digit 4 Left (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     arm_circumference_mm_field = models.CharField(db_column='Arm Circumference (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     elbow_breath_mm_field = models.CharField(db_column='Elbow Breath (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     dart_used_cc_field = models.CharField(db_column='Dart Used (cc)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     pressure_used_bars_field = models.CharField(db_column='Pressure Used (bars)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     processed_forest = models.NullBooleanField(db_column='Processed Forest')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     processed_lab = models.NullBooleanField(db_column='Processed Lab')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     scent_gland_samples = models.CharField(db_column='Scent Gland Samples', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     digit_2_right_mm_field = models.CharField(db_column='Digit 2 Right (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     digit_4_right_mm_field = models.CharField(db_column='Digit 4 Right (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     cranial_circumference_cm_field = models.CharField(db_column='Cranial Circumference (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     milk_expressed = models.NullBooleanField(db_column='Milk Expressed')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     max_thigh_circumference_cm_field = models.CharField(db_column='Max Thigh Circumference (cm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     molar_staining = models.CharField(db_column='Molar Staining', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     premolar_staining = models.CharField(db_column='Premolar Staining', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     incisor_staining = models.CharField(db_column='Incisor Staining', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     canine_staining = models.CharField(db_column='Canine Staining', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     knee_br_femur_mm_field = models.CharField(db_column='Knee Br femur (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     cranial_height_mm_field = models.CharField(db_column='Cranial Height (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     nipple_length_mm_field = models.CharField(db_column='Nipple Length (mm)', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     parasite_types_collected = models.CharField(db_column='Parasite Types Collected', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     parasites_collected = models.NullBooleanField(db_column='Parasites Collected')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fourth_dosage = models.CharField(db_column='Fourth Dosage', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fourth_dosage_time = models.DateTimeField(db_column='Fourth Dosage Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fifth_dosage = models.CharField(db_column='Fifth Dosage', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fifth_dosage_time = models.DateTimeField(db_column='Fifth Dosage Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'capture record'
#
#
# class DatabaseNotes(models.Model):
#     database_notes_id = models.IntegerField(db_column='Database Notes ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
#     notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'database notes'
#
#
# class Demography(models.Model):
#     demography_id = models.IntegerField(db_column='Demography ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     avistaje_id = models.ForeignKey(Avistajes, db_column='Avistaje ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     old_avistaje_number = models.IntegerField(db_column='Old Avistaje Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ams = models.IntegerField(db_column='AMs', blank=True, null=True)  # Field name made lowercase.
#     ams_at_least = models.NullBooleanField(db_column='AMs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ams_ids = models.CharField(db_column='AMs IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sams = models.CharField(db_column='SAMs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     sams_at_least = models.NullBooleanField(db_column='SAMs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sams_ids = models.CharField(db_column='SAMs IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     bams = models.CharField(db_column='BAMs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bams_at_least = models.NullBooleanField(db_column='BAMs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     bams_id = models.CharField(db_column='BAMs ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sms = models.IntegerField(db_column='SMs', blank=True, null=True)  # Field name made lowercase.
#     sms_at_least = models.NullBooleanField(db_column='SMs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sms_ids = models.CharField(db_column='SMs IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jms = models.CharField(db_column='JMs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jms_at_least = models.NullBooleanField(db_column='JMs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jms_id = models.CharField(db_column='JMs ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jm1s = models.CharField(db_column='JM1s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jm1s_at_least = models.NullBooleanField(db_column='JM1s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jm1s_id = models.CharField(db_column='JM1s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jm2s = models.CharField(db_column='JM2s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jm2s_at_least = models.NullBooleanField(db_column='JM2s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jm2s_id = models.CharField(db_column='JM2s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ims = models.CharField(db_column='IMs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ims_at_least = models.NullBooleanField(db_column='IMs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ims_id = models.CharField(db_column='IMs ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     im1s = models.CharField(db_column='IM1s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     im1s_at_least = models.NullBooleanField(db_column='IM1s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     im1s_id = models.CharField(db_column='IM1s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     im2s = models.CharField(db_column='IM2s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     im2s_at_least = models.NullBooleanField(db_column='IM2s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     im2s_id = models.CharField(db_column='IM2s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     afs = models.IntegerField(db_column='AFs', blank=True, null=True)  # Field name made lowercase.
#     afs_at_least = models.NullBooleanField(db_column='AFs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     afs_ids = models.CharField(db_column='AFs IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     afds = models.IntegerField(db_column='AFDs', blank=True, null=True)  # Field name made lowercase.
#     afds_at_least = models.NullBooleanField(db_column='AFDs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     afds_ids = models.CharField(db_column='AFDs IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sfs = models.IntegerField(db_column='SFs', blank=True, null=True)  # Field name made lowercase.
#     sfs_at_least = models.NullBooleanField(db_column='SFs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     sfs_ids = models.CharField(db_column='SFs IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jfs = models.CharField(db_column='JFs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jfs_at_least = models.NullBooleanField(db_column='JFs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jfs_id = models.CharField(db_column='JFs ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jf1s = models.CharField(db_column='JF1s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jf1s_at_least = models.NullBooleanField(db_column='JF1s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jf1s_id = models.CharField(db_column='JF1s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jf2s = models.CharField(db_column='JF2s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     jf2s_at_least = models.NullBooleanField(db_column='JF2s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     jf2s_id = models.CharField(db_column='JF2s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ifs = models.CharField(db_column='IFs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     ifs_at_least = models.NullBooleanField(db_column='IFs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ifs_id = models.CharField(db_column='IFs ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     if1s = models.CharField(db_column='IF1s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     if1s_at_least = models.NullBooleanField(db_column='IF1s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     if1s_id = models.CharField(db_column='IF1s ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     if2s = models.CharField(db_column='IF2s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     if2s_at_least = models.NullBooleanField(db_column='IF2s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     if2s_id = models.CharField(db_column='IF2s ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     adults = models.CharField(db_column='Adults', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     adults_at_least = models.NullBooleanField(db_column='Adults At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     subs = models.CharField(db_column='SUBs', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     subs_at_least = models.NullBooleanField(db_column='SUBs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juvs = models.IntegerField(db_column='JUVs', blank=True, null=True)  # Field name made lowercase.
#     juvs_at_least = models.NullBooleanField(db_column='JUVs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juv1s = models.CharField(db_column='JUV1s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     juv1s_at_least = models.NullBooleanField(db_column='JUV1s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juv2s = models.CharField(db_column='JUV2s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     juv2s_at_least = models.NullBooleanField(db_column='JUV2s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     infs = models.IntegerField(db_column='INFs', blank=True, null=True)  # Field name made lowercase.
#     infs_at_least = models.NullBooleanField(db_column='INFs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf1s = models.CharField(db_column='INF1s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     inf1s_at_least = models.NullBooleanField(db_column='INF1s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf2s = models.CharField(db_column='INF2s', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     inf2s_at_least = models.NullBooleanField(db_column='INF2s At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     unks = models.IntegerField(db_column='UNKs', blank=True, null=True)  # Field name made lowercase.
#     unks_at_least = models.NullBooleanField(db_column='UNKs At Least')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     small_unks = models.CharField(db_column='Small UNKs', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     medium_unks = models.CharField(db_column='Medium UNKs', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     large_unks = models.CharField(db_column='Large UNKs', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     juv_ids = models.CharField(db_column='JUV IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_ids = models.CharField(db_column='INF IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     unk_ids = models.CharField(db_column='UNK IDs', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     demography_comments = models.TextField(db_column='Demography Comments', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_06_present = models.NullBooleanField(db_column='INF 06 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_07_present = models.NullBooleanField(db_column='INF 07 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_08_present = models.NullBooleanField(db_column='INF 08 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_09_present = models.NullBooleanField(db_column='INF 09 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_10_present = models.NullBooleanField(db_column='INF 10 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_11_present = models.NullBooleanField(db_column='INF 11 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_12_present = models.NullBooleanField(db_column='INF 12 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_13_present = models.NullBooleanField(db_column='INF 13 Present')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_06_id = models.CharField(db_column='INF 06 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_07_id = models.CharField(db_column='INF 07 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_08_id = models.CharField(db_column='INF 08 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_09_id = models.CharField(db_column='INF 09 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_10_id = models.CharField(db_column='INF 10 ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_11_id = models.CharField(db_column='INF 11 ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_12_id = models.CharField(db_column='INF 12 ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inf_13_id = models.CharField(db_column='INF 13 ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     total_offspring = models.IntegerField(db_column='Total Offspring', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     total_non_offspring = models.IntegerField(db_column='Total Non-Offspring', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     total_individuals = models.IntegerField(db_column='Total Individuals', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'demography'
#
#
# class DistanceCategories(models.Model):
#     distance_category_id = models.IntegerField(db_column='Distance Category ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     distance_category_sort_id = models.IntegerField(db_column='Distance Category Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     distance_category = models.CharField(db_column='Distance Category', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'distance categories'
#
#
# class Ethogram2008(models.Model):
#     ethogram_2006_id = models.IntegerField(db_column='Ethogram 2006 ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ethogram_2004_id = models.IntegerField(db_column='Ethogram 2004 ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ethogram_2006_sort_id = models.IntegerField(db_column='Ethogram 2006 Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     evento_o_condici_n = models.CharField(db_column='Evento o Condici\xf3n', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     a_azarai = models.CharField(db_column='A azarai', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     a_vociferans = models.CharField(db_column='A vociferans', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     c_discolor = models.CharField(db_column='C discolor', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     a_belzebuth_al = models.CharField(db_column='A belzebuth AL', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ateline_juveniles = models.CharField(db_column='Ateline Juveniles', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     p_monachus = models.CharField(db_column='P monachus', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     condici_n = models.CharField(db_column='Condici\xf3n', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     c_digo_de_comportamiento = models.CharField(db_column='C\xf3digo de Comportamiento', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     description_english = models.CharField(db_column='Description English', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     definition_english = models.TextField(db_column='Definition English', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     descripci_n_espa_ol = models.CharField(db_column='Descripci\xf3n Espa\xf1ol', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     definici_n_espa_ol = models.TextField(db_column='Definici\xf3n Espa\xf1ol', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'ethogram2008'
#
#
# class FeedingBouts(models.Model):
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     feeding_bout_id = models.IntegerField(db_column='Feeding Bout ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     tag_number = models.CharField(db_column='Tag Number', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     begin_eat = models.DateTimeField(db_column='Begin Eat', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     late_start = models.NullBooleanField(db_column='Late Start')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     begin_not_recorded = models.NullBooleanField(db_column='Begin Not Recorded')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_eat = models.DateTimeField(db_column='End Eat', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     early_end = models.NullBooleanField(db_column='Early End')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_not_seen = models.NullBooleanField(db_column='End Not Seen')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_not_recorded = models.NullBooleanField(db_column='End Not Recorded')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     part_eaten = models.CharField(db_column='Part Eaten', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     life_form_if_no_tag = models.CharField(db_column='Life Form If No Tag', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     family_if_no_tag = models.CharField(db_column='Family If No Tag', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     genus_if_no_tag = models.CharField(db_column='Genus If No Tag', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     species_if_no_tag = models.CharField(db_column='Species If No Tag', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     id_by_if_no_tag = models.CharField(db_column='ID By If No Tag', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     max_number_feeders = models.CharField(db_column='Max Number Feeders', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     number_of_feeders_each_min = models.CharField(db_column='Number of Feeders Each Min', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_m = models.CharField(db_column='Loc M', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_deg = models.CharField(db_column='Loc Deg', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_pto_ref = models.CharField(db_column='Loc Pto Ref', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_avg_error = models.CharField(db_column='GPS Avg Error', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_dop = models.CharField(db_column='GPS DOP', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_nav = models.CharField(db_column='GPS Nav', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     leaf_color = models.CharField(db_column='Leaf Color', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fruit_color = models.CharField(db_column='Fruit Color', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     seed_fate = models.CharField(db_column='Seed Fate', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'feeding bouts'
#
#
# class FocalDataAtelines(models.Model):
#     focal_sample_id = models.ForeignKey('FocalSamples', db_column='Focal Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_data_id = models.IntegerField(db_column='Focal Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
#     time_long = models.DateTimeField(db_column='Time Long', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     behavior = models.CharField(db_column='Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     additional_info = models.TextField(db_column='Additional Info', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     partner = models.CharField(db_column='Partner', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nn_id = models.CharField(db_column='NN ID', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_behavior = models.CharField(db_column='NN Behavior', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_distance = models.CharField(db_column='NN Distance', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     infant_id = models.CharField(db_column='Infant ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     infant_behavior = models.CharField(db_column='Infant Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     infant_distance = models.CharField(db_column='Infant Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_composition = models.CharField(db_column='Group Composition', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_m = models.CharField(db_column='Loc M', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_deg = models.CharField(db_column='Loc Deg', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_pto_ref = models.CharField(db_column='Loc Pto Ref', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     utm_x = models.CharField(db_column='UTM X', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     utm_y = models.CharField(db_column='UTM Y', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_avg_error = models.CharField(db_column='GPS Avg Error', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_dop = models.CharField(db_column='GPS DOP', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_navigation = models.CharField(db_column='GPS Navigation', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_carry_infant = models.NullBooleanField(db_column='N2 Carry Infant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_id = models.CharField(db_column='N2 ID', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_behavior = models.CharField(db_column='N2 Behavior', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_partner = models.CharField(db_column='N2 Partner', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_distance = models.CharField(db_column='N2 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     con = models.CharField(db_column='CON', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     field_1 = models.CharField(db_column='<1', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     field_5 = models.CharField(db_column='<5', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     field_10 = models.CharField(db_column='<10', max_length=250, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
#     focal_carry_infant = models.NullBooleanField(db_column='Focal Carry Infant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_carry_infant = models.NullBooleanField(db_column='NN Carry Infant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     list_of_events = models.TextField(db_column='List of Events', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_partner = models.CharField(db_column='NN Partner', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_in_sample = models.CharField(db_column='Time in Sample', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_id = models.CharField(db_column='Voc ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_type = models.CharField(db_column='Voc Type', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_time = models.CharField(db_column='Voc Time', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_loc_m = models.CharField(db_column='Voc Loc M', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_loc_distance = models.CharField(db_column='Voc Loc Distance', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_loc_deg = models.CharField(db_column='Voc Loc Deg', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     voc_loc_pto_ref = models.CharField(db_column='Voc Loc Pto Ref', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     cover = models.CharField(db_column='Cover', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     subject_height = models.CharField(db_column='Subject Height', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     canopy_height = models.CharField(db_column='Canopy Height', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     canopy_zone = models.CharField(db_column='Canopy Zone', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     infant_partner = models.CharField(db_column='Infant Partner', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     exclude_gps_location_data = models.NullBooleanField(db_column='Exclude GPS Location Data')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     at_mineral_lick = models.NullBooleanField(db_column='At Mineral Lick')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     prioritize_biological_samples = models.NullBooleanField(db_column='Prioritize Biological Samples')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     nn_and_inf_scan_point = models.NullBooleanField(db_column='NN and Inf Scan Point')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     is_initiation = models.NullBooleanField(db_column='Is Initiation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     is_response = models.NullBooleanField(db_column='Is Response')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gets_response = models.NullBooleanField(db_column='Gets Response')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'focal data atelines'
#
#
# class FocalDataMonogamous(models.Model):
#     focal_sample_id = models.ForeignKey('FocalSamples', db_column='Focal Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_data_id = models.IntegerField(db_column='Focal Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time = models.CharField(db_column='Time', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     time_long = models.DateTimeField(db_column='Time Long', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     behavior = models.CharField(db_column='Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     additional_info = models.CharField(db_column='Additional Info', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     partner = models.CharField(db_column='Partner', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nearest_neighbor = models.CharField(db_column='Nearest Neighbor', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_carrying_dependent = models.NullBooleanField(db_column='Focal Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n1_id = models.CharField(db_column='N1 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n1_behavior = models.CharField(db_column='N1 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n1_distance = models.CharField(db_column='N1 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n1_partner = models.CharField(db_column='N1 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n1_carrying_dependent = models.NullBooleanField(db_column='N1 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_id = models.CharField(db_column='N2 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_behavior = models.CharField(db_column='N2 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_distance = models.CharField(db_column='N2 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_partner = models.CharField(db_column='N2 Partner', max_length=55, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n2_carrying_dependent = models.NullBooleanField(db_column='N2 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n3_id = models.CharField(db_column='N3 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n3_behavior = models.CharField(db_column='N3 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n3_distance = models.CharField(db_column='N3 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n3_partner = models.CharField(db_column='N3 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n3_carrying_dependent = models.NullBooleanField(db_column='N3 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n4_id = models.CharField(db_column='N4 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n4_behavior = models.CharField(db_column='N4 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n4_distance = models.CharField(db_column='N4 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n4_partner = models.CharField(db_column='N4 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n4_carrying_dependent = models.NullBooleanField(db_column='N4 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n5_id = models.CharField(db_column='N5 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n5_behavior = models.CharField(db_column='N5 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n5_partner = models.CharField(db_column='N5 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n5_distance = models.CharField(db_column='N5 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n5_carrying_dependent = models.NullBooleanField(db_column='N5 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n6_id = models.CharField(db_column='N6 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n6_behavior = models.CharField(db_column='N6 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n6_partner = models.CharField(db_column='N6 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n6_distance = models.CharField(db_column='N6 Distance', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n6_carrying_dependent = models.NullBooleanField(db_column='N6 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n7_id = models.CharField(db_column='N7 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n7_behavior = models.CharField(db_column='N7 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n7_partner = models.CharField(db_column='N7 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n7_distance = models.CharField(db_column='N7 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n7_carrying_dependent = models.NullBooleanField(db_column='N7 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n8_id = models.CharField(db_column='N8 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n8_behavior = models.CharField(db_column='N8 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n8_partner = models.CharField(db_column='N8 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n8_distance = models.CharField(db_column='N8 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n8_carrying_dependent = models.NullBooleanField(db_column='N8 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n9_id = models.CharField(db_column='N9 ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n9_behavior = models.CharField(db_column='N9 Behavior', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n9_partner = models.CharField(db_column='N9 Partner', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n9_distance = models.CharField(db_column='N9 Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     n9_carrying_dependent = models.NullBooleanField(db_column='N9 Carrying Dependent')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     list_of_events = models.TextField(db_column='List of Events', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     actual_time = models.DateTimeField(db_column='Actual Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     check_comments = models.CharField(db_column='Check Comments', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mismatch_jan_2007_jun_2007 = models.NullBooleanField(db_column='Mismatch Jan 2007-Jun 2007')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'focal data monogamous'
#
#
# class FocalSamples(models.Model):
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_animal = models.CharField(db_column='Focal Animal', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_age_sex_class = models.CharField(db_column='Focal Age-Sex Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_start = models.DateTimeField(db_column='Time Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fs_rev_by_pi = models.NullBooleanField(db_column='FS Rev by PI')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fs_rev_by_assistant = models.NullBooleanField(db_column='FS Rev by Assistant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_data_checked_by_pi = models.NullBooleanField(db_column='Focal Data Checked by PI')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_data_checked_by_assistant = models.NullBooleanField(db_column='Focal Data Checked by Assistant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     inter_observer_rel = models.NullBooleanField(db_column='Inter-Observer Rel')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#     dictaphone_file_name = models.CharField(db_column='Dictaphone File Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_end = models.DateTimeField(db_column='Time End', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     dictaphone_used = models.CharField(db_column='Dictaphone Used', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     transcribed = models.NullBooleanField(db_column='Transcribed')  # Field name made lowercase.
#     date_of_transcription = models.DateTimeField(db_column='Date of Transcription', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_early = models.NullBooleanField(db_column='End Early')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_completion = models.CharField(db_column='Focal Completion', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     start_focal_in_sleep_tree = models.NullBooleanField(db_column='Start Focal in Sleep Tree')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     start_sleep_tree_id = models.CharField(db_column='Start Sleep Tree ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_focal_in_sleep_tree = models.NullBooleanField(db_column='End Focal in Sleep Tree')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     end_sleep_tree_id = models.CharField(db_column='End Sleep Tree ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'focal samples'
#
#
# class GeneralActivities(models.Model):
#     general_activity_id = models.IntegerField(db_column='General Activity ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     general_activity_sort_id = models.IntegerField(db_column='General Activity Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     general_activity = models.CharField(db_column='General Activity', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'general activities'
#
#
# class GroupActivities(models.Model):
#     group_activity_id = models.IntegerField(db_column='Group Activity ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_activity_sort_id = models.IntegerField(db_column='Group Activity Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_activity = models.CharField(db_column='Group Activity', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'group activities'
#
#
# class HowEnded(models.Model):
#     how_ended_id = models.IntegerField(db_column='How Ended ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     how_ended = models.CharField(db_column='How Ended', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'how ended'
#
#
# class KindsOfTrees(models.Model):
#     kind_of_tree_id = models.IntegerField(db_column='Kind of Tree ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     kind_of_tree = models.CharField(db_column='Kind of Tree', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'kinds of trees'
#
#
# class LifeForms(models.Model):
#     life_form_id = models.IntegerField(db_column='Life Form ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     life_form = models.CharField(db_column='Life Form', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     life_form_full = models.CharField(db_column='Life Form Full', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'life forms'
#
#
# class LightRainScores(models.Model):
#     light_rain_score_id = models.IntegerField(db_column='Light-Rain Score ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     light_rain_score_sort_id = models.IntegerField(db_column='Light-Rain Score Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     definition = models.CharField(db_column='Definition', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'light-rain scores'
#
#
# class LocationCommentDefinitions(models.Model):
#     location_comments_id = models.IntegerField(db_column='Location Comments ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     location_comments = models.CharField(db_column='Location Comments', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     definition = models.CharField(db_column='Definition', max_length=250, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'location comment definitions'
#
#
# class Locations(models.Model):
#     id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     utmx = models.FloatField(db_column='UTMX', blank=True, null=True)  # Field name made lowercase.
#     utmy = models.FloatField(db_column='UTMY', blank=True, null=True)  # Field name made lowercase.
#     aka_1 = models.CharField(db_column='AKA 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     aka_2 = models.CharField(db_column='AKA 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     category = models.CharField(db_column='Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     object = models.CharField(db_column='Object', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mapping_method = models.CharField(db_column='Mapping Method', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'locations'
#
#
# class MarkedTrees(models.Model):
#     avistaje_id = models.ForeignKey(Avistajes, db_column='Avistaje ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     marked_tree_id = models.IntegerField(db_column='Marked Tree ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     tag_number = models.CharField(db_column='Tag Number', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     aka = models.CharField(db_column='AKA', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     kind_of_tree = models.CharField(db_column='Kind of Tree', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     life_form = models.CharField(db_column='Life Form', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     support_class = models.CharField(db_column='Support Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_m = models.CharField(db_column='Loc M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_deg = models.CharField(db_column='Loc Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_clinometer = models.CharField(db_column='Loc Clinometer', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_pto_ref = models.CharField(db_column='Loc Pto Ref', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     old_loc_pto_ref = models.CharField(db_column='Old Loc Pto Ref', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     cbh = models.FloatField(db_column='CBH', blank=True, null=True)  # Field name made lowercase.
#     cbh_measure_comment = models.CharField(db_column='CBH Measure Comment', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     part_eaten = models.CharField(db_column='Part Eaten', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     family = models.CharField(db_column='Family', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     genus = models.CharField(db_column='Genus', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     species = models.CharField(db_column='Species', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     id_by = models.CharField(db_column='ID By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     alternate_location = models.CharField(db_column='Alternate Location', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     visited_by_pi = models.NullBooleanField(db_column='Visited by PI')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     checked_notes = models.CharField(db_column='Checked Notes', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     comments = models.CharField(db_column='Comments', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     utm_x = models.FloatField(db_column='UTM  X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     utm_y = models.FloatField(db_column='UTM  Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     epe = models.FloatField(db_column='EPE', blank=True, null=True)  # Field name made lowercase.
#     average_error = models.CharField(db_column='Average Error', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     dop = models.CharField(db_column='DOP', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     navigation = models.CharField(db_column='Navigation', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     number_of_points = models.CharField(db_column='Number of Points', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     metal_tag = models.NullBooleanField(db_column='Metal Tag')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     fruit_seed_coll = models.NullBooleanField(db_column='Fruit/Seed Coll')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     leaf_coll = models.NullBooleanField(db_column='Leaf Coll')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     number_leaf_collections = models.CharField(db_column='Number Leaf Collections', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_collection = models.DateTimeField(db_column='Date Collection', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     reviewed_2006 = models.NullBooleanField(db_column='Reviewed 2006')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     collection_location = models.CharField(db_column='Collection Location', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     estimated_dbh = models.IntegerField(db_column='Estimated DBH', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mismatch_jan_2007_jun_2007 = models.NullBooleanField(db_column='Mismatch Jan 2007-Jun 2007')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mapped = models.NullBooleanField(db_column='Mapped')  # Field name made lowercase.
#     on_the_fly_location = models.CharField(db_column='On The Fly Location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'marked trees'
#
#
# class MineralLickVisitData(models.Model):
#     mineral_lick_data_id = models.IntegerField(db_column='Mineral Lick Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.ForeignKey(FocalSamples, db_column='Focal Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     animal_id = models.CharField(db_column='Animal ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_in = models.DateTimeField(db_column='Time In', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_out = models.DateTimeField(db_column='Time Out', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'mineral lick visit data'
#
#
# class MonitoredTrees(models.Model):
#     monitored_tree_id = models.FloatField(db_column='Monitored Tree ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     full_id = models.CharField(db_column='Full ID', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     transect = models.CharField(db_column='Transect', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     comment = models.CharField(db_column='Comment', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     tree_liana = models.CharField(db_column='Tree/Liana', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     block = models.FloatField(db_column='Block', blank=True, null=True)  # Field name made lowercase.
#     quadrat = models.CharField(db_column='Quadrat', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     number = models.FloatField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
#     cbh = models.FloatField(db_column='CBH', blank=True, null=True)  # Field name made lowercase.
#     genus = models.CharField(db_column='Genus', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     species = models.CharField(db_column='Species', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     family = models.CharField(db_column='Family', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     taxonomic_id_by = models.CharField(db_column='Taxonomic ID By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     site = models.CharField(db_column='Site', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'monitored trees'
#
#
# class MorningActivity(models.Model):
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     morning_activity_id = models.CharField(db_column='Morning Activity ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ma_date = models.DateTimeField(db_column='MA_Date', blank=True, null=True)  # Field name made lowercase.
#     ma_time_start = models.DateTimeField(db_column='MA_Time_Start', blank=True, null=True)  # Field name made lowercase.
#     ma_time_end = models.DateTimeField(db_column='MA_Time_End', blank=True, null=True)  # Field name made lowercase.
#     lb_canopy = models.DateTimeField(db_column='LB_Canopy', blank=True, null=True)  # Field name made lowercase.
#     sb_canopy = models.DateTimeField(db_column='SB_Canopy', blank=True, null=True)  # Field name made lowercase.
#     lb_understory = models.DateTimeField(db_column='LB_Understory', blank=True, null=True)  # Field name made lowercase.
#     sb_understory = models.DateTimeField(db_column='SB_Understory', blank=True, null=True)  # Field name made lowercase.
#     obs_green = models.DateTimeField(db_column='Obs_Green', blank=True, null=True)  # Field name made lowercase.
#     obs_yellow = models.DateTimeField(db_column='Obs_Yellow', blank=True, null=True)  # Field name made lowercase.
#     obs_red = models.DateTimeField(db_column='Obs_Red', blank=True, null=True)  # Field name made lowercase.
#     obs_blue = models.DateTimeField(db_column='Obs_Blue', blank=True, null=True)  # Field name made lowercase.
#     def_uri = models.DateTimeField(db_column='Def_Uri', blank=True, null=True)  # Field name made lowercase.
#     mwi = models.DateTimeField(db_column='MWI', blank=True, null=True)  # Field name made lowercase.
#     mbt = models.DateTimeField(db_column='MBT', blank=True, null=True)  # Field name made lowercase.
#     vxx = models.DateTimeField(db_column='VXX', blank=True, null=True)  # Field name made lowercase.
#     feed_start = models.DateTimeField(db_column='Feed Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     tree_tag = models.CharField(db_column='Tree tag', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     food_item = models.CharField(db_column='Food Item', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     food_color = models.CharField(db_column='Food Color', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     food_size = models.CharField(db_column='Food Size', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     feeding_notes = models.CharField(db_column='Feeding Notes', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp1_time = models.DateTimeField(db_column='Other SPP1 Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp1_species = models.CharField(db_column='Other SPP1 Species', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp1_activity = models.CharField(db_column='Other SPP1 Activity', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp2_time = models.DateTimeField(db_column='Other SPP2 Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp2_species = models.CharField(db_column='Other SPP2 Species', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp2_activity = models.CharField(db_column='Other SPP2 Activity', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     other_spp_notes = models.CharField(db_column='Other SPP Notes', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     observer_sample_id = models.CharField(db_column='Observer Sample ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     conditions = models.CharField(db_column='Conditions', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     notes_main = models.CharField(db_column='Notes Main', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'morning activity'
#
#
# class ObsActivityData(models.Model):
#     obs_sample_id = models.ForeignKey('ObserverSamples', db_column='Obs Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     obs_act_data_id = models.IntegerField(db_column='Obs Act Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_start = models.DateTimeField(db_column='Time Start', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time_end = models.DateTimeField(db_column='Time End', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'obs activity data'
#
#
# class ObserverNames(models.Model):
#     observer_name_id = models.IntegerField(db_column='Observer Name ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     observer_name = models.CharField(db_column='Observer Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'observer names'
#
#
class ObserverSamples(models.Model):
    obs_sample_id = models.CharField(db_column='Obs Sample ID', primary_key=True, max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observer = models.CharField(db_column='Observer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time_record_created = models.DateTimeField(db_column='Time Record Created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    gps_used = models.CharField(db_column='GPS Used', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    os_rev_by_pi = models.NullBooleanField(db_column='OS Rev by PI')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    os_rev_by_assistant = models.NullBooleanField(db_column='OS Rev by Assistant')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'observer samples'
#
#
# class PartsEaten(models.Model):
#     part_eaten_id = models.IntegerField(db_column='Part Eaten ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     part_eaten_sort_id = models.IntegerField(db_column='Part Eaten Sort ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     part_eaten = models.CharField(db_column='Part Eaten', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'parts eaten'
#
#
# class PhenoScores(models.Model):
#     pheno_score_id = models.IntegerField(db_column='Pheno Score ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     pheno_score = models.CharField(db_column='Pheno Score', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'pheno scores'
#
#
# class RangingComments(models.Model):
#     ranging_comments_id = models.IntegerField(db_column='Ranging Comments ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_comments = models.CharField(db_column='Ranging Comments', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     definition = models.CharField(db_column='Definition', max_length=250, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'ranging comments'
#
#
# class RangingData(models.Model):
#     avistaje_id = models.CharField(db_column='Avistaje ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_data_id = models.IntegerField(db_column='Ranging Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
#     loc_m = models.CharField(db_column='Loc M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_deg = models.CharField(db_column='Loc Deg', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_pto_ref = models.CharField(db_column='Loc Pto Ref', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_comments = models.CharField(db_column='Ranging Comments', max_length=250, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_activity = models.CharField(db_column='Group Activity', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     light_rain = models.CharField(db_column='Light-Rain', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     wind = models.CharField(db_column='Wind', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     group_speed = models.CharField(db_column='Group Speed', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_spread = models.CharField(db_column='Group Spread', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ranging_notes = models.TextField(db_column='Ranging Notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     associated_with_cebus = models.NullBooleanField(db_column='Associated with Cebus')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     associated_with_lagothrix = models.NullBooleanField(db_column='Associated with Lagothrix')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     associated_with_other = models.NullBooleanField(db_column='Associated with Other')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     cebus_association_distance = models.CharField(db_column='Cebus Association Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     lagothrix_association_distance = models.CharField(db_column='Lagothrix Association Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     check_comments = models.CharField(db_column='Check Comments', max_length=150, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mismatch_jan_2007_jun_2007 = models.NullBooleanField(db_column='Mismatch Jan 2007-Jun 2007')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_avg_err = models.CharField(db_column='GPS Avg Err', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_dop = models.TextField(db_column='GPS DOP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     gps_navigation = models.CharField(db_column='GPS Navigation', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     associated_with = models.CharField(db_column='Associated With', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     association_distance = models.CharField(db_column='Association Distance', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_height = models.CharField(db_column='Group Height', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     canopy_height = models.CharField(db_column='Canopy Height', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     utm_x = models.IntegerField(db_column='UTM X', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     utm_y = models.IntegerField(db_column='UTM Y', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     utm_source = models.CharField(db_column='UTM Source', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     over_flood = models.NullBooleanField(db_column='Over Flood')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     loc_in_sleeping_tree = models.NullBooleanField(db_column='Loc in Sleeping Tree')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     on_the_fly_location = models.CharField(db_column='On The Fly Location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     weather_score = models.CharField(db_column='Weather Score', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     at_mineral_lick = models.NullBooleanField(db_column='At Mineral Lick')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     exclude_loc_data = models.NullBooleanField(db_column='Exclude Loc Data')  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     focal_sample_id = models.CharField(db_column='Focal Sample ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     prox_data = models.TextField(db_column='Prox Data', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group_composition = models.TextField(db_column='Group Composition', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     prox_visibility = models.CharField(db_column='Prox Visibility', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'ranging data'
#
#
# class RollCallDemography(models.Model):
#     avistaje_id = models.ForeignKey(Avistajes, db_column='Avistaje ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     roll_call_demography_id = models.IntegerField(db_column='Roll Call Demography ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     obs_sample_linked = models.CharField(db_column='Obs Sample Linked', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     obs_sample_id = models.CharField(db_column='Obs Sample ID', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     animal_name = models.CharField(db_column='Animal Name', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     group = models.CharField(db_column='Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(db_column='Status', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'roll call demography'
#
#
# class SupportClasses(models.Model):
#     support_class_id = models.IntegerField(db_column='Support Class ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     support_class = models.CharField(db_column='Support Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     support_class_full = models.CharField(db_column='Support Class Full', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'support classes'
#
#
# class TaxonNames(models.Model):
#     taxon_id = models.IntegerField(db_column='Taxon ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     taxon_name = models.CharField(db_column='Taxon Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'taxon names'
#
#
# class TrailNames(models.Model):
#     trail_id = models.IntegerField(db_column='Trail ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     trail_name = models.CharField(db_column='Trail Name', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     trail_code = models.CharField(db_column='Trail Code', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = True
#         db_table = 'trail names'
#
#
# class Transects(models.Model):
#     transect_id = models.IntegerField(db_column='Transect ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     transect = models.CharField(db_column='Transect', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'transects'
#
#
# class WeatherData(models.Model):
#     obs_sample_id = models.ForeignKey(ObserverSamples, db_column='Obs Sample ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     weather_data_id = models.IntegerField(db_column='Weather Data ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
#     score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
#     light_rain = models.CharField(db_column='Light-Rain', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     wind = models.CharField(db_column='Wind', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     comments = models.CharField(db_column='Comments', max_length=200, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'weather data'
#
#
# class WindScores(models.Model):
#     wind_score_id = models.IntegerField(db_column='Wind Score ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     definition = models.CharField(db_column='Definition', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'wind scores'
# ##[jetbrains/Users/reedd/Documents/projects/pycharm/paleocore18/proyecto.models
