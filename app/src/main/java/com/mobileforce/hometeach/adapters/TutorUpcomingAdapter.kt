package com.mobileforce.hometeach.adapters

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.mobileforce.hometeach.R
import com.mobileforce.hometeach.models.Schedule
import com.squareup.picasso.Picasso
import de.hdodenhof.circleimageview.CircleImageView
import kotlinx.android.synthetic.main.upcoming_classes_tutor.view.*
import java.text.SimpleDateFormat
import java.util.*

class TutorUpcomingAdapter(private val itemsList: List<Schedule>) :
    RecyclerView.Adapter<TutorUpcomingAdapter.RecyclerViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerViewHolder {

        val items = LayoutInflater.from(parent.context)
            .inflate(
                R.layout.upcoming_classes_tutor, parent
                , false
            )
        return TutorUpcomingAdapter.RecyclerViewHolder(items)
    }

    override fun getItemCount(): Int {
        return itemsList.size
    }

    override fun onBindViewHolder(holder: RecyclerViewHolder, position: Int) {
     holder.initialise(itemsList[position])
    }


    class RecyclerViewHolder(itemview: View) : RecyclerView.ViewHolder(itemview) {
        val studentImage:CircleImageView = itemview.tutor_image
        val subject:TextView = itemview.subject_name
        val date:TextView = itemview.class_date
        val time = itemview.class_time

        fun initialise(data:Schedule){
            subject.text=data.subject
            time.text = "${data.from_hour}:${data.from_minute}-${data.to_hour}:${data.to_minute}"

            val format = SimpleDateFormat("dd-MM-yyyy", Locale.US)
            val r = format.parse(data.)
            date.text = r.toString()

            Picasso.get().load(data.student_pic).transform(CircleTransform())
                .error(R.drawable.profile_image).into(studentImage)
        }

    }

}